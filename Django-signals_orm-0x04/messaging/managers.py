from django.db import models

class UnreadMessagesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(read=False)

    def unread_for_user(self, user):
        """Get unread messages for a specific user"""
        return self.get_queryset().filter(receiver=user)