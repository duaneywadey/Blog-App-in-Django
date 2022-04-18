from django.urls import path
from .import views
from .views import logout_view
from django.contrib.auth import views as authView



urlpatterns = [
	path('sign_up/', views.sign_up, name='users-sign-up'),
	path('profile/', views.profile, name='users-profile'),
	path('login/', authView.LoginView.as_view(template_name='users/login.html'), name='users-log-in'),
	path('logout/', views.logout_view, name='users-log-out'), 
	path('chatboard/', views.chatboard, name='users-chatboard'),
	path('delete/<int:pk>/', views.deleteMessage, name='users-chatboard-delete'),



]	