from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('login/', views.LoginView, name='login'),
    path('profile/', views.ProfileView, name='profile'),
    path('edit_profile/', views.Edit_ProfileView, name='edit_profile'),
    path('logout/', views.LogoutView, name='logout'),
]
