
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentications.urls')),
    path('', views.home, name='home'),
]
