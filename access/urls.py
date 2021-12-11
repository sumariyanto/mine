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
   path('api/v1/userpage-range',views.UserPageList.as_view(),name='page_list_user'),
   path('api/v1/userpage-offset',views.UserPageOffset.as_view(),name='page_offset'),
   path('api/v1/login',views.UserLogin.as_view(),name='sdfa'),
   path('api/v1/logout',views.UserLogout.as_view(),name='logut'),
]
