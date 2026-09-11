from django.urls import path
from .import views

urlpatterns = [
   path("<int:pk>/", views.recommendation_detail, name="recommendation_detail"),
]


