from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from django.contrib.auth import get_user_model

from posts.models import Follow, Post, Group, Comment
from .serializers import (FollowSerializer, PostSerializer, GroupSerializer,
                          CommentSerializer)
from .permissions import IsGroupAdminOnly, IsAuthorPost, IsAuthorComment

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorPost, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    # permission_classes = (IsGroupAdminOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorComment, )

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs['post_id']))

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        # comments = Comment.objects.filter(post=post)
        return post.comments


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
    queryset = Follow.objects.all()

    def get_queryset(self):
        """Возвращает queryset c подписками для текущего пользователя."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer: FollowSerializer):
        """Создает подписку, где подписчиком является текущий пользователь."""
        serializer.save(user=self.request.user)
