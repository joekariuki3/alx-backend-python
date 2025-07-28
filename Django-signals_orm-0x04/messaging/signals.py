from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Message, Notification

@receiver(post_save, sender=Message)
def send_notification_to_message_receiver(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(recipient=instance.receiver, message=instance)