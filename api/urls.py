from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import ProductList, UserList, RatingList

urlpatterns = [
    path('user/', UserList.as_view()),
    path('product/', ProductList.as_view()),
    path('rating/', RatingList.as_view()),
    path('api-auth-token/', ObtainAuthToken.as_view()),
]
