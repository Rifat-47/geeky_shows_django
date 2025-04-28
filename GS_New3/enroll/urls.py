from django.urls import path
from . import views

urlpatterns = [
    path('stu/', views.studentinfo, name='all_students'),
    path('regi/', views.showformdata),
    path('success/', views.thankyou),
    path('stu/<stu_id>/', views.studentinfo, name='student_detail'),
    path('regi/stu', views.student_form, name='student_reg'),
    path('regi/tchr', views.teacher_form, name='teacher_reg'),

]
