from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import BlogPost


def blog_home(request):

    posts = BlogPost.objects.all().order_by("-created_at")

    # Search
    query = request.GET.get("q", "").strip()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(excerpt__icontains=query) |
            Q(content__icontains=query)
        )

    # Category filter
    category = request.GET.get("category", "").strip()

    if category:
        posts = posts.filter(category=category)

    # Featured post
    if query or category:
        featured_post = None
        latest_posts = posts
    else:
        featured_post = posts.filter(is_featured=True).first()

        if featured_post:
            latest_posts = posts.exclude(id=featured_post.id)
        else:
            latest_posts = posts

    return render(
        request,
        "blogs/blog.html",
        {
            "featured_post": featured_post,
            "posts": latest_posts,
            "query": query,
            "category": category,
        }
    )


def blog_detail(request, slug):

    post = get_object_or_404(
        BlogPost,
        slug=slug
    )

    # Increase view count
    post.views += 1
    post.save(update_fields=["views"])

    return render(
        request,
        "blogs/blog_detail.html",
        {
            "post": post
        }
    )