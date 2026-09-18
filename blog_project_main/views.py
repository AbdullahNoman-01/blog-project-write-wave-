from django.db.models import Count, Avg, Sum, Subquery, OuterRef
from django.shortcuts import render, get_object_or_404
from recommendations.models import Recommendation
from posts.models import Like, Post, Rating, Tags

def home(request):

    # Average rating subquery
    rating_avg = Rating.objects.filter(
        post=OuterRef("pk")
    ).values("post").annotate(
        average=Avg("score")
    ).values("average")

    # Get all liked post IDs of current user only once
    liked_post_ids = set()

    if request.user.is_authenticated:
        liked_post_ids = set(
            Like.objects.filter(
                user=request.user
            ).values_list("post_id", flat=True)
        )

    # Optimized posts queryset
    posts = (
        Post.objects
        .select_related("author")
        .prefetch_related("tags")
        .annotate(
            like_count=Count(
                "likes",
                distinct=True
            ),
            average_rating=Subquery(rating_avg)
        )
        .order_by("-created_at")
    )

    # Set like status without database query
    for post in posts:
        post.is_liked = post.id in liked_post_ids

    # Admin recommendations
    recommendations = (
        Recommendation.objects
        .filter(is_published=True)
        .order_by("-created_at")
    )

    # All tags
    tags = Tags.objects.all().order_by("name")

    return render(
        request,
        "home.html",
        {
            "posts": posts,
            "recommendations": recommendations,
            "tags": tags,
        }
    )


def posts_by_tag(request, tag_id):

    tag = get_object_or_404(
        Tags,
        id=tag_id
    )

    posts = (
        tag.posts
        .select_related("author")
        .prefetch_related("tags")
        .annotate(
            like_count=Count(
                "likes",
                distinct=True
            ),
            total_rating=Sum("ratings__score")
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "posts_by_tag.html",
        {
            "tag": tag,
            "posts": posts,
        }
    )