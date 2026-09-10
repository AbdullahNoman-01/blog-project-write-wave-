from django.db.models.aggregates import Count
from django.shortcuts import render
from posts.models import Like, Post

# Create your views here.
def home(request):
   posts = Post.objects.all(). annotate(like_count=Count("likes")).order_by("-created_at")
   for post in posts:
        post.is_liked = (
            request.user.is_authenticated
            and Like.objects.filter(
                user=request.user,
                post=post
            ).exists()
        )
   return render(request, 'home.html', {'posts': posts})