from rest_framework import viewsets, status, filters, permissions, response
from rest_framework.decorators import action
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer
from .permissions import IsConversationParticipant, IsMessageSender

class ConversationViewSet(viewsets.ModelViewSet):
    """
    A Viewset for viewing and editing conversation instances.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated, IsConversationParticipant]

    def perform_create(self, serializer):
        """
        When creating a conversation, automatically add the current user as a participant.
        """
        conversation = serializer.save()
        if self.request.user not in conversation.participants.all():
            conversation.participants.add(self.request.user) # .add() adds and saves, many to many relation

    @action(detail=True, methods=['post'], url_path='send-message')
    def send_message(self, request, pk=None):
        """
        Custom action to send a message to a specific conversation.
        Expected data: {"message_body": "Your message content here"}
        """
        try:
            conversation = self.get_object()
        except Conversation.DoesNotExist:
            return response.Response({"detail": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)

        # Ensure the user is a participant before allowing them to send a message
        if not conversation.participants.filter(user_id=request.user.user_id).exists():
            return response.Response({"detail": "You are not a participant in this conversation."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(sender_id=request.user.id, conversation=conversation)
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        """
        Restrict the returned conversations to those
        that the current user is a participant of.
        """
        if self.request.user.is_authenticated:
            return Conversation.objects.filter(participants=self.request.user).order_by('-created_at')
        return Conversation.objects.none() # return empty queryset is not authenticated

class MessageViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, and editing message instances.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Message.objects.all().order_by('-sent_at')
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated, IsMessageSender]

    def get_queryset(self):
        """
        Filters messages to ensure only messages from conversations the user participates in are visible.
        If nested, it will filter by the specific conversation.
        """
        if self.request.user.is_authenticated:

            # Check if this viewset is nested under a conversation (/conversations/{id}/messages/)
            conversation_pk = self.kwargs.get('conversation_pk')
            if conversation_pk:
                try:
                    conversation = Conversation.objects.get(conversation_id=conversation_pk)
                    # If user is not participant.
                    if not conversation.participants.filter(user_id=self.request.user.user_id).exists():
                        # return empty queryset
                        return Message.objects.none()
                    return Message.objects.filter(conversation__conversation_id=conversation_pk).order_by('sent_at')
                except Conversation.DoesNotExist:
                    return Message.objects.none()

            # Fallback for top-level /messages/ endpoint, showing all messages from user's conversations
            # This fetches messages from ALL conversations the user is a part of.
            user_conversations = Conversation.objects.filter(participants=self.request.user)
            return Message.objects.filter(conversation__in=user_conversations).order_by('sent_at')

    def perform_create(self, serializer):
        print(self.kwargs)
        conversation_pk = self.kwargs.get('conversation_pk')
        if not conversation_pk:
            raise serializer.ValidationError({"conversation": "This field is required when creating a message directly."})
        try:
            conversation = Conversation.objects.get(conversation_id=conversation_pk)
        except Conversation.DoesNotExist:
            raise serializer.ValidationError({"conversation": "Conversation not found."})

        # Ensure the user is a participant of the target conversation
        if not conversation.participants.filter(user_id=self.request.user.user_id).exists():
            raise serializer.ValidationError(
                {"detail": "You can only send messages to conversations you are a participant of."})

        serializer.save(sender=self.request.user, conversation=conversation)