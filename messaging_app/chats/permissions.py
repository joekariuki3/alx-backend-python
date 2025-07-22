from rest_framework import permissions

class IsConversationParticipant(permissions.BasePermission):
    """
    Custom permission to only allow participants of a conversation to view or interact with it
    """
    message = "You are not a participant of this conversation"

    def has_object_permission(self, request, view, obj):
        """
        Determines if the user has permission to access a specific Conversation object.

        This method checks whether the requesting user is a participant of
        the Conversation object. It verifies the user's presence in the object's
        participant list and returns the result.

        Parameters:
        request: The HTTP request object containing user information.
        view: The current view instance handling the request.
        obj (Conversation instance): The object for which the permission check is performed.

        Returns:
        bool: True if the user is a participant of the object, False otherwise.
        """
        return obj.participants.filter(user_id=request.user.user_id).exists()


class IsMessageSender(permissions.BasePermission):
    """
    Custom permission to only allow the sender of a message to update or delete it.
    Read access (GET) is allowed for any participants of the conversation.
    """
    message = "You are not the sender of this message"

    def has_object_permission(self, request, view, obj):
        """
        Determines whether a user has the required permissions to access or modify the Message object.

        This method assesses user permissions based on the HTTP request method. For safe methods,
        it checks if the user is a participant in the corresponding conversation. For modification
        attempts, it verifies if the user is the sender of the Message object.

        Args:
            request: The HTTP request object containing details of the request.
            view: The view the user is trying to access.
            obj (Message instance): The object being accessed or modified.

        Returns:
            bool: True if the user has the necessary permissions, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return obj.conversation.participants.filter(user_id=request.user.user_id).exists()
        return obj.sender_id == request.user.user_id