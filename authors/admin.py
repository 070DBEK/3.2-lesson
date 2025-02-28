from django.contrib import admin
from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "bio", 'user')
    search_fields = ("name", "email")
    list_filter = ("email", 'user')
    ordering = ("name",)