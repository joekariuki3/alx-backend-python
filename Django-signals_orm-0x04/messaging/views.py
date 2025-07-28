from .models import User, Message, Notification, MessageHistory
from .serializers import UserSerializer, MessageSerializer , NotificationSerializer, MessageHistorySerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer
