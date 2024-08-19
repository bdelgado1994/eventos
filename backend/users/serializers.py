from typing import Dict, Any

from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User=get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data=super().validate(attrs)
        data['user']=UserSerializer(self.user).data
        return data