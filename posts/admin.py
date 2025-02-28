from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "category", "status", "created_at")
    search_fields = ("title", "author__name", "category__name")
    list_filter = ("status", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-created_at",)