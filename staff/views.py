from django.shortcuts import render, get_object_or_404
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
    permission_classes = []


class ResourceViewset(viewsets.ModelViewSet):
    serializer_class = ResourceSerializer
    permission_classes = []


class MultipleFieldLookupMixin:
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs.get(field): # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj


class CollectionViewset(MultipleFieldLookupMixin,viewsets.ModelViewSet):
    serializer_class = CollectionSerializer
    permission_classes = []
    queryset = Collection.objects.all()
    lookup_fields = ['student', 'resource']