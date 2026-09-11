from django.db import models

# Create your models here.

class BlogPost(models.Model):

    CATEGORY_CHOICES = [
        ("Technology", "Technology"),
        ("Programming", "Programming"),
        ("Education", "Education"),
        ("Lifestyle", "Lifestyle"),
        ("Career", "Career"),
    ]

    title = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        max_length=220
    )

    excerpt = models.TextField(
        max_length=300
    )

    content = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    featured_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    views = models.PositiveIntegerField(
        default=0
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