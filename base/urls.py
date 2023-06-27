from django.urls import path
from .views import CustomLogin, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login', CustomLogin.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', Register.as_view(), name='register'),
]
