from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import ProductView, UserView, RatingView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('product/', ProductView.as_view()),
    path('rating/', RatingView.as_view()),
    path('api-auth-token/', ObtainAuthToken.as_view()),
]
