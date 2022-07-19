from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewSet, GroupViewSet, PostViewSet

from rest_framework.authtoken import views


router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register(
    'posts/(?P<post_id>\\d+)/comments', CommentViewSet, basename='comments'
)
router.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
