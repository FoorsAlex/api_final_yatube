from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename=r'posts/(?P<post_id>\d+)/comments'
                )
router.register(r'follow',
                FollowViewSet,
                basename=r'follow')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
