from django.urls import path
from .views import login_page, register_page, home, error, logout, password_change, activate_email


urlpatterns = [
    path('', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('home/', home, name='home'),
    path('error/', error, name='error'),
    path('logout/', logout, name='logout'),
    path('password_change/', password_change, name='password_change'),
    path('activate/<email_token>/' , activate_email , name="activate_email"),
    
]
