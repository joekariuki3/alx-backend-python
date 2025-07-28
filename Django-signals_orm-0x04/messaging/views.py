from rest_framework.response import Response

from .models import User, Message, Notification, MessageHistory
from .serializers import UserSerializer, MessageSerializer , NotificationSerializer, MessageHistorySerializer
from rest_framework import viewsets, status


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class MessageHistoryViewSet(viewsets.ModelViewSet):
    queryset = MessageHistory.objects.all()
    serializer_class = MessageHistorySerializer

def delete_user(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)