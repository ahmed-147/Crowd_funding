from django.urls import path
from .views import (
    add_comment,
    report_comment
)
app_name = "comment"
urlpatterns = [
    path('add/<int:pk>', add_comment, name='add_comment'),
    path('report/<int:pk>/<int:projectPk>', report_comment, name='report_comment'),

]
