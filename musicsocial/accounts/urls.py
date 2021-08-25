from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('<int:pk>/profile/', views.ShowProfilePageView.as_view(), name='profile'),

]
