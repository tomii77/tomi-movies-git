from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("simple_function", views.simple_function),
    path("todays_movies", views.todays_movies),
]