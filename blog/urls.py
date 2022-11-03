from django.urls import path

from blog import views

urlpatterns = [
    path('', views.about, name='blog-about'),
    path('projects', views.projects, name='blog-projects'),
]