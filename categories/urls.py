from django.conf.urls import url
from . import views


urlpatterns = [url(r'^homepage/$', views.homepage, name='homepage'),
               url(r'^computer-science/$', views.cs, name='cs'),
               url(r'^business/$', views.business, name='business'),
               url(r'^astronomy/$', views.astronomy, name='astronomy')]
