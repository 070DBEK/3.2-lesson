from rest_framework import serializers
from .models import Comment


class RecursiveCommentSerializer(serializers.Serializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveCommentSerializer(many=True, read_only=True)
    author_email = serializers.EmailField()

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