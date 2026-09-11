from django.urls import path
from .import views

urlpatterns = [
   path('create-post/', views.CreatePost, name='create_post'),
   path('like-post/<int:pk>/', views.like_post, name='like_post'),
   path('edit-post/<int:pk>/', views.Edit_Post, name='edit_post'),
   path('delete-post/<int:pk>/', views.delete_post, name='delete_post'),
   path('post-detail/<int:pk>/', views.post_detail, name='post_detail'),
   path('notifications/', views.Notifications, name='notifications'),
]
