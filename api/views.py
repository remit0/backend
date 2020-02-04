from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product, Rating
from .permissions import IsPostOrIsAuthenticated
from .serializers import ProductSerializer, UserSerializer, RatingSerializer


class UserList(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsPostOrIsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get('username', None)
        if username is not None:
            return User.objects.filter(username=username)
        return User.objects.all()


class ProductList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RatingList(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION').replace("Token ", "")
        data = request.data.dict()
        data["user"] = Token.objects.get(key=token).user_id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Invalid request')
