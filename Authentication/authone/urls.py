from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.UserRegistration),
    path('login', views.UserLogin),

]
