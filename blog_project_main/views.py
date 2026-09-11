from django.db.models import Count
from django.shortcuts import render
from recommendations.models import Recommendation
from posts.models import Like, Post


def home(request):

    posts = Post.objects.all().annotate(
        like_count=Count("likes")
    ).order_by("-created_at")

    # Like status
    for post in posts:
        post.is_liked = (
            request.user.is_authenticated
            and Like.objects.filter(
                user=request.user,
                post=post
            ).exists()
        )

    # Admin recommendations
    recommendations = Recommendation.objects.filter(
        is_published=True
    ).order_by("-created_at")

    return render(
        request,
        "home.html",
        {
            "posts": posts,
            "recommendations": recommendations,
        }
    )