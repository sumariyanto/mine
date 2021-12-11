
from django.urls import path
from django.conf import settings
from .views import *
from . import views


urlpatterns = [
   path('api/v1/contact', views.Contact_V1.as_view()),
   path('api/v1/contact/<int:pk>',views.ContactDetail_v1.as_view(),name='contact-detail'),
   path('api/v1/register-user',views.AddRegisterUser.as_view(),name='register'),
   path('api/v1/register-user/<int:id>',views.DetailUser.as_view(),name='detail-user'),
  
]
