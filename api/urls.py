from django.urls import path
from .views import delete_details, get_details, create_details, update_details, patch_details
from rest_framework.decorators import api_view, permission_classes
urlpatterns = [
    path('get/', get_details),

    path('create/', create_details),

    path('update/<int:id>/', update_details),

    path('patch/<int:id>/', patch_details),

    path('delete/<int:id>/', delete_details),
]
