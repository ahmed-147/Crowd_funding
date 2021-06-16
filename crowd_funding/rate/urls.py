from django.urls import path
from .views import (
    add_rate
)
app_name = "rate"
urlpatterns = [
    path('add/<int:pk>', add_rate, name='add_rate'),

]
