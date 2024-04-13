from .models import Profile, Details
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # exclude = ['name', 'age', ]
        #include
        fields = '__all__'



class DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        exclude = ['photo']
        


