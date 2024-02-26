from django.urls import path
from staticpages.views import AboutProjectView


app_name = 'staticpages'

urlpatterns = [
    path('about/', AboutProjectView.as_view(), name='about'),
]
