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
        exclude = ["bill"]


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = "__all__"

    
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = "__all__"
        read_only_fields = ["collection_date", "return_date", "expired", "collection_id"]
    
    def validate(self, data):
        try:
            student = Student.objects.get(reg_no=data['reg_no'])
            resource = Resource.objects.get(resource_id=data['resource_id'])
            return data
        except Student.DoesNotExist:
            raise serializers.ValidationError("The student does not exist")
        except Resource.DoesNotExist:
            raise serializers.ValidationError("The resource does not exist")