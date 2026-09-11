from django.contrib import admin
from .models import BlogPost

# Register your models here.


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "is_featured",
        "views",
        "created_at",
    )

    list_filter = (
        "category",
        "is_featured",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
        "excerpt",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }