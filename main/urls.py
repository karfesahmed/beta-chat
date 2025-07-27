from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('get-messages/', views.get_messages, name='get_messages'),
    path('send-message/', views.send_message, name='send_message'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
]