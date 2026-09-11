from django.db import models

# Create your models here.
from django.db import models


class Recommendation(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField(
        max_length=500
    )
    content = models.TextField()
    image = models.ImageField(
        upload_to="recommendations/",
        blank=True,
        null=True
    )
    is_published = models.BooleanField(
        default=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    class Meta:
        ordering = ["-created_at"]
    def __str__(self):
        return self.title