from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "author", "content", "created_at", "parent_comment")
    search_fields = ("post__title", "author__name", "content")
    list_filter = ("created_at",)
    ordering = ("-created_at",)

