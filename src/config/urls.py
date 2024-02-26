from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls'), name='articles'),
    path('', include('staticpages.urls'), name='staticpages'),
    path('', include('users.urls'), name='users'),
    path('', include('django.contrib.auth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
