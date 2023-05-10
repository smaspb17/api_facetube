from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FollowViewSet, PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('follow', FollowViewSet)
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
