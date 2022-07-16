from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from posts.models import Group, Post
from .serializers import (CommentSerializer,
                          GroupSerializer, PostSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer