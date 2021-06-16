from django.urls import path
from .views import (
    user_login,
    user_logout,
    user_register,
    show_profile,
    edit_profile,
    activate,
)
app_name = "user_profile"
urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', user_register, name='user_register'),
    path('user/<int:pk>/', show_profile, name='show_profile'),
    path('edit/<int:pk>/', edit_profile, name='edit_profile'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate')
]
