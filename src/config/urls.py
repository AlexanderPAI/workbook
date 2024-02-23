from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls'), name='articles'),
    path('', include('users.urls'), name='users'),
    path('', include('django.contrib.auth.urls')),
]
