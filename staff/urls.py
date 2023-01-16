from django.urls import path, include
from .views import *


app_name = 'staff'

student = StudentViewset.as_view({
    'post':'create'
})
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('student/', student, name='student')
]