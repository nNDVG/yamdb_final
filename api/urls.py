from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import CategoriesList, GenresList, TitlesViewSet, UserViewSet

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')
v1_router.register(r'titles', TitlesViewSet)
v1_router.register(r'categories', CategoriesList)
v1_router.register(r'genres', GenresList)


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/auth/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh')

]
