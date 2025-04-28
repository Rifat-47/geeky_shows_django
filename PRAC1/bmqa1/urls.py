from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('reg/', views.registration, name='registration'),
    path('success/', views.success, name='success'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),

]