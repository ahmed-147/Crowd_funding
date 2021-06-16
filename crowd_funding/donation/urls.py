from django.urls import path
from .views import (
    add_donation
)
app_name = "donation"
urlpatterns = [
    path('add/<int:pk>', add_donation, name='add_donation'),
]
