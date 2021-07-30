from rest_framework import serializers
from collection.models import Collection, APIRequest
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}


class APIRequestSerializer(serializers.ModelSerializer):
    # created_by = UserSerializer(read_only=True)

    class Meta:
        model = APIRequest
        fields = (
            'id',
            'collection',
            'request_header',
            'request_body',
            'created_by',
            'created_at',
            'updated_at'
        )
