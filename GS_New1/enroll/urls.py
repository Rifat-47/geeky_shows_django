from django.urls import path
from . import views

urlpatterns = [
    path('stu/', views.studentinfo),
    path('regi/', views.showformdata),
    path('success/', views.thankyou)
]
