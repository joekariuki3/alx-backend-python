import django_filters
from .models import Message

class MessageFilter(django_filters.FilterSet):
    conversation = django_filters.UUIDFilter(field_name='conversation__conversation_id')
    sender = django_filters.UUIDFilter(field_name='sender__user_id')
    sent_at_after = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_at_before = django_filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')
    message = django_filters.CharFilter(field_name='message_body', lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ['conversation', 'sender', 'sent_at_after', 'sent_at_before', 'message']