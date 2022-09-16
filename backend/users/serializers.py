from rest_framework import serializers
from django.contrib.auth.models import User

# A serializer is a component that converts Django models to JSON objects and vice-versa.
class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username' ,'email', 'name', 'password')