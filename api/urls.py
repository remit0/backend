from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token

from .views import ProductList, ProductDetail


urlpatterns = [
    path('product/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('api-auth-token/', obtain_auth_token, name='api_auth_token'),
]
