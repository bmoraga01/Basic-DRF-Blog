from rest_framework.permissions import BasePermission
from ..models import Comment

class IsOwnerOrReadAndCreateOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'POST'):
            return True
        else:
            id_comment = view.kwargs['pk']
            comment = Comment.objects.get(pk=id_comment)
            
            return comment.user.pk == request.user.pk