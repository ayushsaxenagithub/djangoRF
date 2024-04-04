from .models import Person
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        meta = Person
        # exclude = ['name', 'age', ]
        fields = "__all__"