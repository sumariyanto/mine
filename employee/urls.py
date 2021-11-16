from django.urls import path
from .views import *
from  .import views

urlpatterns=[
    path('api/v1/employee',views.EmployeeListView.as_view(),name='employee-list'),
    path('api/v1/employee/<int:pk>',views.EmployeeDetailView.as_view(),name='employee-detail'),
    path('api/v1/bagian',views.BagianList_Apiv1.as_view(),name="bagian"),
    path('api/v1/bagian/<int:pk>',views.BagianDetail_Apiv1.as_view(),name="bagian-detail"),
    path('api/v1/golongan',views.GolonganList_Apiv1.as_view(), name='golongan'),
]