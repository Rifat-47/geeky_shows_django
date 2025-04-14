from django.urls import path
from . import views

urlpatterns = [
    path('stu/', views.studentinfo, name='all_students'),
    path('regi/', views.showformdata),
    path('success/', views.thankyou),
    path('stu/<stu_id>/', views.studentinfo, name='student_detail'),
]
