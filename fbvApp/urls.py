from django.urls import path
from fbvApp import views

urlpatterns = [
    path('students/', views.student_list),
    path('students/<int:pk>', views.student_detail)
]