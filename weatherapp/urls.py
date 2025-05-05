# weatherapp/urls.py
from django.urls import path
from .views.home_view import home_view_render

urlpatterns = [
    path('', home_view_render , name='home'),  # or whatever your view is
]
