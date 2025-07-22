from rest_framework import viewsets, status, filters, permissions, response
from .models import Conversation, Message, User
from .serializers import ConversationSerializer, MessageSerializer, UserSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    """
    A Viewset for viewing and editing conversation instances.
    Provides list, create, retrieve, update, and destroy actions.
    """
    queryset = Conversation.objects.all().order_by('-created_at')
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        When creating a conversation, automatically add the current user as a participant.
        """
        conversation = serializer.save()
        if self.request.user not in conversation.participants.all():
            conversation.participants.add(self.request.user)
            conversation.save()

    def send_message(self, request, pk=None):
        """
        Custom action to send a message to a specific conversation.
        Expected data: {"message_body": "Your message content here"}
        """
        try:
            conversation = self.get_object()
        except Conversation.DoesNotExist:
            return response.Response({"detail": "Conversation not found."}, status=status.HTTP_404_NOT_FOUND)

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
        return super().get_queryset()

class MessageViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, and editing message instances.
    Provides list, create, retrieve, update, and destroy actions.
    """
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        conversation_pk = self.kwargs.get('conversation_pk')
        if conversation_pk:
            return Message.objects.filter(conversation__conversation_id=conversation_pk).order_by('sent_at')
        return Message.objects.all().order_by('sent_at')

    def perform_create(self, serializer):
        conversation_pk = self.kwargs.get('conversation_conversation_pk')
        conversation = Conversation.objects.get(conversation_id=conversation_pk)
        serializer.save(sender=self.request.user, conversation=conversation)

    def get_queryset(self):
        """
        Filter messages by conversation ID, if provided in the URL.
        """
        conversation_pk = self.kwargs.get('conversation_pk') # Assuming a nested URL structure
        if conversation_pk:
            return Message.objects.filter(conversation__conversation_id=conversation_pk).order_by('sent_at')
        return super().get_queryset()
