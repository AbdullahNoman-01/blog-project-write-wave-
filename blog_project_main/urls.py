from django.contrib import admin
from django.urls import path,include
from .import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentications.urls')),
    path('posts/', include('posts.urls')),
    path('recommendations/', include('recommendations.urls')),
    path('blogs/', include('blogs.urls')),
    path('', views.home, name='home'),
    path('tags/<int:tag_id>/', views.posts_by_tag, name='posts_by_tag'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
