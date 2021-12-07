from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('', include('Tour.urls')),
    path('admin/', admin.site.urls),
    path('blog/',include(('blog.urls','blog'),namespace = 'blog')),
    path('users/',include(('users.urls','users'),namespace = 'users')),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
