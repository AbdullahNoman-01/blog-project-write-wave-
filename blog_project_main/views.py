from django.db.models import Count
from django.shortcuts import render,get_object_or_404
from recommendations.models import Recommendation
from posts.models import Like, Post,Tags


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
    tag = get_object_or_404(Tags, id=tag_id)
    posts = tag.posts.all().annotate(
        like_count=Count("likes")
    ).order_by("-created_at")
    return render(
        request,
        "posts_by_tag.html",
        {
            "tag": tag,
            "posts": posts,
        }
    )