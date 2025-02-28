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

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                author = Author.objects.get(user=request.user)
                validated_data['author'] = author
            except Author.DoesNotExist:
                raise serializers.ValidationError({"author": "User has no author profile."})
        else:
            raise serializers.ValidationError({"author": "User must be authenticated."})
        category_id = self.initial_data.get('category')
        if category_id:
            try:
                validated_data['category'] = Category.objects.get(id=category_id)
            except Category.DoesNotExist:
                raise serializers.ValidationError({"category": "Invalid category ID."})
        tag_ids = self.initial_data.get('tags', [])
        tags = Tag.objects.filter(id__in=tag_ids)
        validated_data['slug'] = validated_data.get('slug') or slugify(validated_data['title'])
        post = Post.objects.create(**validated_data)
        post.tags.set(tags)
        return post
