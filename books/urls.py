from django.urls import path
from .views import index, show
urlpatterns = [
    path('book/<id>', show,name="book_details"),
    path('index', index),
]