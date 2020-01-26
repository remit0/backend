from django.urls import path

from .views import CustomObtainAuthToken, ProductList, ProductDetail, UserList, UserDetail

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>', ProductDetail.as_view()),
    path('api-auth-token/', CustomObtainAuthToken.as_view()),
]
