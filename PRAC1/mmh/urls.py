from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('creg/', views.customer_registration, name='customer registration'),

]