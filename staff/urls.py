from django.urls import path, include
from .views import *

app_name = 'staff'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]