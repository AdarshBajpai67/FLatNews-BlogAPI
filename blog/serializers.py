from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Post
        exclude = ('updated_at',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = get_user_model()
        fields = ('id', 'username')
