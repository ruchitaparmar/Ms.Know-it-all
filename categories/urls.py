from django.conf.urls import url
from . import views


urlpatterns = [url(r'^homepage/$', views.homepage, name='homepage'),
               url(r'^computer-science/$', views.cs, name='cs'),
               url(r'^business/$', views.business, name='business'),
               url(r'^astronomy/$', views.astronomy, name='astronomy'),
               url(r'^homepage-search$', views.searchHome, name='homepageS'),
               url(r'^computer-science-search$', views.searchCs, name='csS'),
               url(r'^business-search$', views.searchBusiness, name='businessS'),
               url(r'^astronomy-search$', views.searchAstronomy, name='astronomyS')]
