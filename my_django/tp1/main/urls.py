from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='homePage'),
    path('about', views.about, name='aboutUsPage'),
    path('create', views.create, name='create')
]

urlpatterns += staticfiles_urlpatterns()