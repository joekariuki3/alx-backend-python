from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register('conversations', ConversationViewSet)
routers.register('messages', MessageViewSet)


urlpatterns = [
    path('', include(routers.urls)),
]