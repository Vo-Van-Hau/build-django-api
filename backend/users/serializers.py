from rest_framework import serializers
from .models import Users

# A serializer is a component that converts Django models to JSON objects and vice-versa.
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('username' ,'email', 'name', 'password')