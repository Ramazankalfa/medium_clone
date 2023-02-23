from django.contrib import admin
from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'is_active']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'is_active']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'is_active', 'view_count']