from rest_framework import serializers
from .models import Comment
from authors.models import Author


class RecursiveCommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'replies']

    def get_replies(self, obj):
        return RecursiveCommentSerializer(obj.replies.all(), many=True).data



class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveCommentSerializer(many=True, read_only=True)
    author_name = serializers.CharField(write_only=True)
    author_email = serializers.EmailField(write_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'author_name', 'author_email', 'content', 'created_at', 'parent_comment', 'replies']

    def validate_parent_comment(self, value):
        if value:
            level = 1
            parent = value
            while parent.parent_comment:
                level += 1
                parent = parent.parent_comment
                if level >= 3:
                    raise serializers.ValidationError("Maximum comment nesting level (3) exceeded.")
        return value

    def validate_author_email(self, value):
        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError("Only Gmail addresses are allowed.")
        return value

    def create(self, validated_data):
        author_name = validated_data.pop('author_name')
        author_email = validated_data.pop('author_email')

        author, created = Author.objects.get_or_create(email=author_email, defaults={'name': author_name})
        validated_data['author'] = author

        return super().create(validated_data)