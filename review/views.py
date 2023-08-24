from rest_framework.viewsets import ModelViewSet
from .models import Comment, Like, Rating
from .serializers import CommentSerializer, RatingSerializer
from rest_framework.permissions import AllowAny
from post.permissions import IsAdminOrIsAuthenticatedPermission, IsAuthorPermission


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [IsAdminOrIsAuthenticatedPermission]

        elif self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthorPermission]
        
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class CommentView(PermissionMixin, ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# class RatingView(PermissionMixin, ModelViewSet):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer

#     def check_action(self):
#         if self.action == 'create':











