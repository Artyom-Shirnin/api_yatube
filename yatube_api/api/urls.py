from rest_framework import routers

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
]
