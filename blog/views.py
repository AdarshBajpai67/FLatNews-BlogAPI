from django.shortcuts import render
from rest_framework import generics

from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer