from django.urls import path
from .views import add_category, show_categories, edit_category
app_name = "category"
urlpatterns = [
    path('add/', add_category, name='add_category'),
    path('show_categories/', show_categories, name='show_categories'),
    path('edit/<int:pk>', edit_category, name='edit_category'),


]
