from django.urls import path
from django.conf import settings
from .views import *
from .import views

urlpatterns =[
   path('api/v1/access', views.AccessListApi.as_view(),name='access'),
   path('api/v1/access/<int:pk>', views.AccessDetailApi.as_view(),name='access_detail'),
   path('api/v1/spost',views.AccessPostApi.as_view(),name="post-access"),
]
