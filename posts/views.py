from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required


from posts.models import Like, Notification, Post

# Create your views here.
@login_required
def CreatePost(request):
   if request.method == 'POST':
       form = PostForm(request.POST, request.FILES)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.save()
           form.save_m2m()
           return redirect('home')
   else:
       form = PostForm()
   return render(request, 'posts/create_post.html', {'form': form})


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
    return redirect(request.META.get("HTTP_REFERER", "home"))


@login_required
def Edit_Post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect("home")
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "posts/edit_post.html", {
        "form": form,
        "post": post,
    })


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return redirect("home")
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, "posts/delete_post.html", {
        "post": post
    })



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by("-created_at")
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            # Create notification
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    sender=request.user,
                    post=post,
                    notification_type="comment",
                    message=f"{request.user.username} commented on your post."
                )
            return redirect("post_detail", pk=post.pk)
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



@login_required
def Notifications(request):
    notifications = Notification.objects.filter(
        recipient=request.user
    ).order_by("-created_at")
    return render(
        request,
        "posts/notification_post.html",
        {
            "notifications": notifications
        }
    )


