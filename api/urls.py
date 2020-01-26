from django.urls import path

from .views import CustomObtainAuthToken, ProductList, ProductDetail

urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('api-auth-token/', CustomObtainAuthToken.as_view(), name='api_auth_token'),
]
