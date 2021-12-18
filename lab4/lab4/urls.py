

from django.contrib import admin
from django.urls import path
from BMSTU import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetDepartments, name = 'main'),
    path('department/<str:name>/', views.GetDepartment, name = "department_url")
]
