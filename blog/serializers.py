from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Post
        fields = (
            'author',
            'title',
            'body',
            'thumbnail',
            'created_at',
        )
