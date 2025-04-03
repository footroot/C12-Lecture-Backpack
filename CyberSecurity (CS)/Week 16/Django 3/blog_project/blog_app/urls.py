from django.urls import path
from .views import create_blog, view_blog, home, delete_blog

urlpatterns = [
    path('create/', create_blog, name='create_blog'),
    path('view/<int:blog_id>', view_blog, name="view_blog"),
    path('delete/<int:blog_id>', delete_blog, name="delete_blog"),
    path('', home, name='home'),
]