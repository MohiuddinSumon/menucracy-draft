from django.urls import path
from .views import RegisterEmployeeAPI, RegisterRestaurantAPI, LoginRestaurantAPI, LoginEmployeeAPI

app_name = 'account'

urlpatterns = [
    path('register-employee/', RegisterEmployeeAPI.as_view(), name='register-employee'),
    path('register-restaurant/', RegisterRestaurantAPI.as_view(), name='register-employee'),
    path('login-employee/', LoginEmployeeAPI.as_view(), name='register-employee'),
    path('login-restaurant/', LoginRestaurantAPI.as_view(), name='register-employee'),
]
