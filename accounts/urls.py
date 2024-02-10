from django.urls import path
from .views import UserLogin, UserRegister

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', UserRegister.as_view(), name='register')
]