from django.urls import path

from .views import index

urlpatterns = [
    path('', index, name='blog-about'),
    path('giga/<int:pk>/<int:pkk>', index),
]