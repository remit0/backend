from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product, Rating
from .permissions import IsPostOrIsAuthenticated
from .serializers import ProductSerializer, UserSerializer, RatingSerializer


class UserView(generics.ListCreateAPIView):

    serializer_class = UserSerializer
    permission_classes = [IsPostOrIsAuthenticated]

    def get_queryset(self):
        username = self.request.query_params.get(key="username")
        if username is not None:
            return User.objects.filter(username=username)
        return User.objects.all()


class ProductView(generics.ListCreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RatingView(generics.ListCreateAPIView, generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        try:
            # required
            user = User.objects.get(id=self.request.user.id)
            name = request.data.get("name")
            value = request.data.get("value")
            # optional
            year = request.data.get("year")
            store = request.data.get("store")
            comment = request.data.get("comment")
            type = request.data.get("type")
            vol = request.data.get("vol")
            # processing args
            product = Product(name=name, year=year, store=store, type=type, vol=vol)
            product.save()
            rating = Rating(user=user, product=product, value=value, comment=comment)
            rating.save()
            return Response("Successfully added the new rating !")

        except Exception as e:
            print(e)
            return Response("Could not add the new rating.")

    def delete(self, request, *args, **kwargs):
        try:
            rating_id = request.data.get("id")
            Rating.objects.get(id=rating_id).delete()
            return Response(f"Successfully deleted the rating with id {rating_id}")

        except Exception as e:
            print(e)
            return Response("Could not delete the rating.")
