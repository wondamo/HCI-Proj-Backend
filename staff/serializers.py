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
        user = Staff.objects.get(email=obj['email'])
        return user.tokens()


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        extra_kwargs = {'password': {'write_only':True, 'min_length':6}}
        exclude = ['is_staff', 'is_active', 'is_superuser', 'id', 'last_login']

    def create(self, data):
        password = data.pop('password', None)
        staff = Staff.objects.create_user(**data)
        staff.set_password(password)
        staff.save()
        return staff

    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"