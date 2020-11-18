from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:pk>", views.blog_specific, name="blog_post"),
]
