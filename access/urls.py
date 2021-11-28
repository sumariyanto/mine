from django.urls import path
from django.conf import settings
from .views import *
from .import views

urlpatterns =[
   path('api/v1/access', views.AccessListApi.as_view(),name='access'),
   path('api/v1/access/<int:pk>', views.AccessDetailApi.as_view(),name='access_detail'),
   path('api/v1/spost',views.AccessPostApi.as_view(),name="post-access"),
   path('api/v1/userlist',views.UserListApi.as_view(),name='user_list'),
   path('api/v1/user-page',views.UserPage.as_view(),name='sd'),
]
