from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['user_id']


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.CharField(source='sender.username', read_only=True)
    receiver_name = serializers.CharField(source='receiver.username', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'conversation', 'sender', 'receiver', 'message_body', 'send_at', 'created_at']
        read_only_fields = ['message_id', 'send_at', 'created_at']

    def validate_message_body(self, value):
        if not value.strip():
            raise serializers.ValidationError("Message content cannot be empty.")
        return value


class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at', 'updated_at', 'last_message']
        read_only_fields = ['conversation_id', 'created_at', 'updated_at']

    def get_last_message(self, obj):
        last_message = obj.messages.order_by('-timestamp').first()
        if last_message:
            return {
                'message_body': last_message.message_body,
                'sender': last_message.sender.username,
                'timestamp': last_message.timestamp
            }
        return None

    def validate(self, data):
        if 'participants' in self.initial_data and not self.initial_data['participants']:
            raise serializers.ValidationError("A conversation must have at least one participant.")
        return data