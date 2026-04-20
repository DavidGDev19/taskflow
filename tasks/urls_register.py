from django.urls import path
from tasks.views import register

urlpatterns = [
    path('', register, name='register'),
]
