from django.urls import path
from info.views import AboutView


app_name = 'info'

urlpatterns = [
    path('about/', AboutView, name='about'),
]
