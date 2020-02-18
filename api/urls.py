from django.conf.urls.static import static
from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from backend import settings
from .views import ProductView, UserView, RatingView, ImageView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('product/', ProductView.as_view()),
    path('rating/', RatingView.as_view()),
    path('api-auth-token/', ObtainAuthToken.as_view()),
    path('image/', ImageView.as_view())
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
