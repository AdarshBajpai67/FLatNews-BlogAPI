from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer


class PostViewset(viewsets.ModelViewSet):
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


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer