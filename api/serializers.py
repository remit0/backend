from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product, Rating, Image


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'year', 'store', 'type', 'vol', 'id']


class RatingSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = Rating
        fields = ['value', 'product', 'date', 'user', 'id', 'comment']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

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


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ["image", "product"]
