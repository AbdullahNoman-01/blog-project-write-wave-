from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Prefetch

from posts.forms import PostForm, CommentForm
from posts.models import Comment, Like, Notification, Post, Rating


# Create Post
@login_required
def CreatePost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()

            return redirect("home")

    else:
        form = PostForm()

    return render(
        request,
        "posts/create_post.html",
        {"form": form}
    )


# Like / Unlike Post
@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if created:

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                sender=request.user,
                post=post,
                notification_type="like",
                message=f"{request.user.username} liked your post."
            )

    else:
        like.delete()

    return redirect(
        request.META.get("HTTP_REFERER", "home")
    )


# Edit Post
@login_required
def Edit_Post(request, pk):

    post = get_object_or_404(
        Post.objects.select_related("author"),
        pk=pk
    )

    if post.author != request.user:
        return redirect("home")

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()

            return redirect(
                "post_detail",
                pk=post.pk
            )

    else:
        form = PostForm(instance=post)

    return render(
        request,
        "posts/edit_post.html",
        {
            "form": form,
            "post": post,
        }
    )


# Delete Post
@login_required
def delete_post(request, pk):

    post = get_object_or_404(
        Post.objects.select_related("author"),
        pk=pk
    )

    if post.author != request.user:
        return redirect("home")

    if request.method == "POST":
        post.delete()
        return redirect("home")

    return render(
        request,
        "posts/delete_post.html",
        {
            "post": post
        }
    )


# Post Detail
def post_detail(request, pk):

    # Optimized Post Query
    post = get_object_or_404(
        Post.objects
        .select_related("author")
        .annotate(
            average_rating=Avg("ratings__score")
        )
        .prefetch_related(
            "tags",
            "ratings",
            Prefetch(
                "comments",
                queryset=Comment.objects
                .filter(parent__isnull=True)
                .select_related("user")
                .prefetch_related(
                    Prefetch(
                        "replies",
                        queryset=Comment.objects
                        .select_related("user")
                        .order_by("created_at")
                    )
                )
                .order_by("-created_at")
            )
        ),
        pk=pk
    )

    # Because comments are already prefetched
    comments = post.comments.all()

    if request.method == "POST":

        if not request.user.is_authenticated:
            return redirect("login")

        comment_form = CommentForm(request.POST)

        if comment_form.is_valid():

            comment = comment_form.save(commit=False)

            comment.post = post
            comment.user = request.user

            parent_id = request.POST.get("parent_id")

            if parent_id:

                parent_comment = get_object_or_404(
                    Comment,
                    id=parent_id,
                    post=post
                )

                comment.parent = parent_comment

            comment.save()

            # Notification
            if comment.parent:

                # Reply notification
                if comment.parent.user != request.user:

                    Notification.objects.create(
                        recipient=comment.parent.user,
                        sender=request.user,
                        post=post,
                        notification_type="comment",
                        message=(
                            f"{request.user.username} "
                            f"replied to your comment."
                        )
                    )

            else:

                # Normal comment notification
                if post.author != request.user:

                    Notification.objects.create(
                        recipient=post.author,
                        sender=request.user,
                        post=post,
                        notification_type="comment",
                        message=(
                            f"{request.user.username} "
                            f"commented on your post."
                        )
                    )

            return redirect(
                "post_detail",
                pk=post.pk
            )

    else:
        comment_form = CommentForm()

    return render(
        request,
        "posts/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
        }
    )


# Notifications
@login_required
def Notifications(request):

    notifications = (
        Notification.objects
        .filter(recipient=request.user)
        .select_related(
            "sender",
            "recipient",
            "post"
        )
        .order_by("-created_at")
    )

    return render(
        request,
        "posts/notification_post.html",
        {
            "notifications": notifications
        }
    )


# Rate Post
@login_required
def rate_post(request, pk):

    post = get_object_or_404(
        Post,
        pk=pk
    )

    if request.method == "POST":

        score = int(
            request.POST.get("score", 0)
        )

        if score < 1 or score > 5:

            messages.error(
                request,
                "Rating must be between 1 and 5."
            )

            return redirect(
                "post_detail",
                pk=post.pk
            )

        Rating.objects.update_or_create(
            post=post,
            user=request.user,
            defaults={
                "score": score
            }
        )

        messages.success(
            request,
            "Your rating has been saved!"
        )

    return redirect(
        "post_detail",
        pk=post.pk
    )