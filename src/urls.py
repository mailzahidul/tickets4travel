from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accounts/login/', views.userLogin, name='login'),
    path('accounts/logout/', views.userLogout, name='user_logout'),
    path('web/user/', views.webUser, name='web_user'),
]