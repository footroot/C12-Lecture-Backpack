from django.urls import path
from .views import home, welcome

urlpatterns = [
    path('home/', home, name='home'),
    path('welcome/', welcome, name='welcome')
]