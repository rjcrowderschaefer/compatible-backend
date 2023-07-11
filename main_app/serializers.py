from rest_framework import serializers
from .models import TestClass

class TestClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestClass
        fields = ('name', 'field_one', 'field_two')