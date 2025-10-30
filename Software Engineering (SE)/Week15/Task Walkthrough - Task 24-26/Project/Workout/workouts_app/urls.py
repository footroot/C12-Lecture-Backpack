# workout_app/urls.py
from django.urls import path
from .views import get_all, get, create, update, delete

urlpatterns = [
   path('', get_all, name='show_workouts'),
   path('<int:pk>', get, name='get_workout'),
   path('new/', create, name='create_workout'),
   path('<int:pk>/edit', update, name='update_workout'),
   path('<int:pk>/delete', delete, name='delete_workout'),
]
