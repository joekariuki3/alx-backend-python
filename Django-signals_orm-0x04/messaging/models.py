from django.db import models
from django.contrib.auth.models import User

class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(read=False)

    def for_user(self, user):
        """Get unread messages for a specific user"""
        return self.get_queryset().filter(receiver=user).only(
            'sender',
            'receiver',
            'content',
            'timestamp'
        )


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    parent_message = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    read = models.BooleanField(default=False)
    objects = models.Manager()
    unread_messages = UnreadMessagesManager()

class Notification(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message')
    seen = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

class MessageHistory(models.Model):
    edited = models.TextField(null=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    edited_at = models.DateTimeField(auto_now_add=True)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='edited_by')