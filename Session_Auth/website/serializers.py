from .models import UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    class Meta:
        meta = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    


class UserProfileSerializer(serializers.Serializer):
    class Meta:
        meta = UserProfile 
        fields = '__all__'
                