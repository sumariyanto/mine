from django.urls import path
from .views import *
from  .import views

urlpatterns=[
    path('api/v1/employee',views.EmployeeListView.as_view(),name='employee-list'),
    path('api/v1/employee/<int:pk>',views.EmployeeDetailView.as_view(),name='employee-detail'),
]