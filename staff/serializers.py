from rest_framework import serializers, exceptions
from .models import *

# create your serializers here

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=68, write_only=True)
    tokens = serializers.SerializerMethodField()

    def validate(self, attrs):
        email, password = attrs['email'], attrs['password']
        user = Staff.objects.get(email=email)
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid credentials try again")
        return attrs
        
    def get_tokens(self, obj):
        user = Staff.objects.get(email=obj.email)
        return user.tokens()