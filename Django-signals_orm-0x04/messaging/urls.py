from django.urls import path, include
from rest_framework_nested import routers
from .views import UserViewSet, MessageViewSet, NotificationViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet, basename='message')
router.register('notifications', NotificationViewSet, basename='notification')
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]