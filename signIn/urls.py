from django.conf.urls import url
from . import views


urlpatterns = [url(r'^register/$', views.register, name='register'),
               url(r'^$', views.signInBeta, name='profile')]
