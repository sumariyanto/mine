from django.urls import path
from .views import *
from  .import views

urlpatterns=[
    path('api/v1/index', views.Lembur_list.as_view(),name='lembur')
]