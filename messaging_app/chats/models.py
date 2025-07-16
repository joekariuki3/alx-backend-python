from django.db import models
from django.contrib.auth.models import User


class User(User):
    """
    Custom User model that extends the default Django User model.
    """

    # custom fields and methods goes here
    pass


class Conversation(models.Model):
    """
    Model that tracks which users are involved in a conversation.
    """

    participants = models.ManyToManyField(User, related_name="conversations")


class Message(models.Model):
    """
    Model containing the sender, receiver, and content of a message.
    """

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
