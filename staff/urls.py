from django.urls import path, include
from .views import *


app_name = 'staff'

student = StudentViewset.as_view({
    'post':'create',
    'get':'list',
})

resource = ResourceViewset.as_view({
    'post':'create',
    'get':'list',
})

collection = CollectionViewset.as_view({
    'post':'create',
    'put':'update',
})

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('student/', student, name='student'),
    path('resource/', resource, name='resource'),
    path('collection/', collection, name='collection'),
]