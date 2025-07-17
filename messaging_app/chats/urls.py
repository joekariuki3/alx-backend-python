from django.urls import path
from .views import ConversationViewSet, MessageViewSet

urlpatterns = [
    path('conversations/', ConversationViewSet.as_view({'get': 'list'})),
    path('conversations/<int:pk>/', ConversationViewSet.as_view({'get': 'retrieve'})),
    path('conversations/<int:pk>/messages/', MessageViewSet.as_view({'get': 'list'})),
    path('conversations/<int:pk>/messages/<int:msg_pk>/', MessageViewSet.as_view({'get': 'retrieve'})),
]