from rest_framework import serializers
from django.utils.text import slugify
from .models import Post
from categories.models import Category
from tags.models import Tag
from authors.models import Author
from comments.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, required=False
    )

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'content', 'author', 'category', 'tags', 'slug',
            'created_at', 'updated_at', 'status', 'comment_count', 'comments'
        ]
        extra_kwargs = {
            'slug': {'read_only': True},
        }

    def get_comment_count(self, obj):
        return obj.comments.count()

