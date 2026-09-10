from django.shortcuts import render,redirect

from posts.models import Post
from .import forms

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def SignUpView(request):
   if request.method == 'POST':
      form = forms.SignUpForm(request.POST)
      if form.is_valid():
         form.save()
         messages.add_message(request, messages.SUCCESS, "Account Create Successfully")
         return redirect('login')
   else:
      form = forms.SignUpForm()

   context = {
      'form':form
   }
   return render(request, 'authentications/signup.html', context)


def LoginView(request):
   if request.method == "POST":
      form = AuthenticationForm(data = request.POST)
      if form.is_valid():
         username = form.cleaned_data.get('username')
         password = form.cleaned_data.get('password')

         user = authenticate(
               username=username,
               password=password
         )
         if user is not None:
               login(request, user)
               messages.success(
                  request,
                  "Login Successfully"
               )
               return redirect("home")
         else:
               messages.error(
                  request,
                  "Invalid username or password"
               )
   else:
      form = AuthenticationForm()

   context = {
       'form':form
   }

   return render(request, "authentications/login.html",context)



@login_required
def ProfileView(request):

    user_posts = Post.objects.filter(
        author=request.user
    ).order_by("-created_at")

    return render(
        request,
        "authentications/profile.html",
        {
            "user_posts": user_posts,
        }
    )


@login_required
def Edit_ProfileView(request):
   user = request.user
   if request.method == "POST":
      user.username = request.POST.get("username")
      user.first_name = request.POST.get("first_name")
      user.last_name = request.POST.get("last_name")
      user.email = request.POST.get("email")
      user.save()
      messages.success(request, "Your profile has been updated successfully!")
      return redirect("profile")
   return render(request, "authentications/edit_profile.html")


@login_required
def LogoutView(request):
   logout(request)
   messages.add_message(request, messages.SUCCESS, "Logout Successfully")
   return redirect('home')

