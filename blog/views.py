from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        author = self.request.user
        status = serializer.validated_data['status']

        # Allow only admins to save posts as draft
        if not author.is_staff:
            status = 'published'

        return serializer.save(status=status, author=author)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
