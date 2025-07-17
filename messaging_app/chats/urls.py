from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('conversations', ConversationViewSet)
router.register('messages', MessageViewSet)


urlpatterns = [
    path('', include(router.urls)),
]