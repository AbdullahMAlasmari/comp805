#FLASHCARDS URL CONF
from django.urls import path

from . import views

app_name='flashcards'
urlpatterns = [
    path('', views.home, name='home'),
]
