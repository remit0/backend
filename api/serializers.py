from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product, Rating


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'year', 'store', 'type']


class RatingSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Rating
        fields = ['rating', 'product', 'date', 'user']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        super().update(instance, validated_data)
        return instance
