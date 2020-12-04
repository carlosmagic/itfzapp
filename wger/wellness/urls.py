from django.conf.urls import include
from django.urls import path
from wger.wellness import views
from django.contrib.auth.models import User
urlpatterns = [
    path('add/', views.add_wellness, name='add_wellness')
]