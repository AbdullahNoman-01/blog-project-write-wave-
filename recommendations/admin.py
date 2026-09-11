from django.contrib import admin
from .models import Recommendation
# Register your models here.
from django.contrib import admin
from .models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "is_published",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "is_published",
        "created_at",
    )

    search_fields = (
        "title",
        "short_description",
        "content",
    )

    ordering = (
        "-created_at",
    )