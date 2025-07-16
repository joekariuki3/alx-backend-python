from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class User(User):
    """
    Custom User model that extends the default Django User model.
    """

    user_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


class Conversation(models.Model):
    """
    Model that tracks which users are involved in a conversation.
    """

    conversation_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    participants = models.ManyToManyField(User, related_name="conversations")


class Message(models.Model):
    """
    Model containing the sender, receiver, and content of a message.
    """

    message_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
