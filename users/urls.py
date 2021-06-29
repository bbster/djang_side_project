from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.create_account, name='account'),
    path('user_list/', views.user_list, name='user_list'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]