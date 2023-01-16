from django.shortcuts import render
from rest_framework import generics, views, response, status, viewsets, permissions
from .serializers import *

# Create your views here.

class LoginView(generics.GenericAPIView):
    '''
    This is the login view for the application for the staffs
    '''
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        except Staff.DoesNotExist:
            return response.Response("Staff does not exist", status=status.HTTP_400_BAD_REQUEST)

    
class RegisterView(generics.GenericAPIView):
    '''
    This is the view for registering staffs in the application
    '''
    serializer_class = StaffSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)

class StudentViewset(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]