from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('employees/', views.employee_list, name='employee_list'),
    path('employees/<int:id>/', views.employee_detail, name='employee_detail'),

    path('projects/', views.project_list, name='project_list'),
    path('projects/<int:id>/', views.project_detail, name='project_detail'),
]