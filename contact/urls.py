
from django.urls import path
from django.conf import settings
from .views import *
from . import views


urlpatterns = [
   path('api/v1/contact', views.Contact_V1.as_view()),
  
]
