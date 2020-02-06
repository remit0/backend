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
        username = self.request.query_params.get()
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

    def post(self, request, *args, **kwargs):
        try:
            token = request.META.get("HTTP_AUTHORIZATION").replace("Token ", "")
            user_id = Token.objects.get(key=token).user_id
            user = User.objects.get(id=user_id)

            name = request.data.get("name")
            year = request.data.get("year", default=-1)
            store = request.data.get("store", default="-")
            rating = request.data.get("rating")

            new_product = Product(name=name, year=year, store=store)
            new_product.save()
            product_rating = Rating(user=user, product=new_product, rating=rating)
            product_rating.save()

            return Response("Succeeded")

        except Exception as e:
            print(e)
            return Response("Invalid request")
