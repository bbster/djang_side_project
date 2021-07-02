from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('user_list/', views.UserList.as_view()),
]
