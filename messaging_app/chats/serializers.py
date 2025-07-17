from rest_framework import serializers
from .models import User, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'email', 'password', 'first_name', 'last_name', 'phone_number']
        read_only_fields = ['user_id']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'receiver', 'message_body', 'sent_at', 'created_at']
        read_only_fields = ['message_id', 'created_at', 'sent_at']


class ConversationListSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'last_message']
        read_only_fields = ['conversation_id']

    def get_last_message(self, obj):
        last_message = obj.messages.order_by('-timestamp').first()
        if last_message:
            return MessageSerializer(last_message).data
        return None


class ConversationDetailSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    participant_ids = serializers.ListField(
        child=serializers.UUIDField(),
        write_only=True,
        required=False
    )

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages',
                  'participant_ids', 'created_at', 'updated_at']
        read_only_fields = ['conversation_id', 'created_at', 'updated_at']

    def create(self, validated_data):
        participant_ids = validated_data.pop('participant_ids', [])
        conversation = Conversation.objects.create(**validated_data)

        # Add participants to the conversation
        participants = User.objects.filter(user_id__in=participant_ids)
        conversation.participants.add(*participants)

        # Add the requesting user as a participant
        user = self.context['request'].user
        if user not in participants:
            conversation.participants.add(user)

        return conversation
