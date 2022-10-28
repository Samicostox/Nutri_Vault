from rest_framework import serializers
from .models import Preferences, User, Physic

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'name', 'username', 'email', 'password']

class PhysicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Physic
        fields = ['id','height','weight','goal','duration','user']

class PreferencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Preferences
        fields = ['id', 'fav_ingredients', 'fav_crountry_meal','budget','fav_complexity','fav_meals','user']