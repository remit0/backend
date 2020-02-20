from django.contrib.auth.models import User
from django.http import FileResponse
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from backend.settings import MEDIA_ROOT
import os
from .models import Product, Rating, Image
from .permissions import IsPostOrIsAuthenticated
from .serializers import ProductSerializer, UserSerializer, RatingSerializer, ImageSerializer


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


class RatingView(generics.ListCreateAPIView, generics.DestroyAPIView, generics.UpdateAPIView):

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

    def put(self, request, *args, **kwargs):
        try:
            product_attributes = [key for key in request.data.keys() if key in Product.get_attributes()]
            rating_attributes = [key for key in request.data.keys() if key in Rating.get_attributes()]
            rating = Rating.objects.get(id=request.data.get(key="id"))
            if rating_attributes:
                for attribute in rating_attributes:
                    val = request.data.get(key=attribute)
                    if attribute == "value":
                        val = int(float(val))
                    setattr(rating, attribute, val)
                rating.save()
            if product_attributes:
                product = rating.product
                for attribute in product_attributes:
                    setattr(product, attribute, request.data.get(key=attribute))
                product.save()
            return Response(f"Successfully updated")

        except Exception as e:
            print(e)
            return Response("Could not update the rating.")

    def patch(self, request, *args, **kwargs):
        raise NotImplementedError


class ImageView(generics.CreateAPIView, generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser, FileUploadParser]

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response("Success", status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        try:
            image = Image.objects.filter(product__id=request.GET.get("id")).first()
            serializer = self.serializer_class(image)
            img = open(MEDIA_ROOT + serializer.data.get("image"), "rb")
            return FileResponse(img, status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("Failed", status.HTTP_400_BAD_REQUEST)

    # TODO : PUT, DELETE
