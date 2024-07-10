from django.urls import path
from info.views import AboutView, MailReceiver


app_name = 'info'

urlpatterns = [
    path('about/', AboutView, name='about'),
    path('receiver.html', MailReceiver, name='mail_receiver'),
]
