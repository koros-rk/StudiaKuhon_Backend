from django.contrib import admin
from djoser.views import TokenCreateView, TokenDestroyView
from django.urls import path, include, re_path
from rest_framework import routers

from disign_shop.views import *
from disign_shop.TelegramOrder import OrderView
from furniture_shop.views import *

design_shop_router = routers.DefaultRouter()

# Design shop
design_shop_router.register(r'products', ProductViewSet, basename='products')
design_shop_router.register(r'styles', StyleViewSet, basename='style')
design_shop_router.register(r'materials', MaterialViewSet, basename='materials')
design_shop_router.register(r'palettes', PaletteViewSet, basename='palettes')
design_shop_router.register(r'photos', PhotoViewSet, basename='photos')
design_shop_router.register(r'handles', HandleViewSet, basename='handles')

furniture_shop_router = routers.DefaultRouter()

# Furniture shop
furniture_shop_router.register(r'furniture', FurnitureViewSet, basename='furniture')
furniture_shop_router.register(r'categories', CategoryViewSet, basename='categories')
furniture_shop_router.register(r'photos', FurniturePhotoViewSet, basename='photos')
furniture_shop_router.register(r'colors', FurnitureColorViewSet, basename='colors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/design_shop/', include(design_shop_router.urls)),
    path('api/v1/furniture_shop/', include(furniture_shop_router.urls)),
    path('api/v1/order', OrderView.as_view()),
    path('api/v1/gallery', ProductGallery.as_view()),
    path('api/v1/auth2', include('rest_framework.urls')),
    path('api/v1/auth/token/create/', TokenCreateView.as_view()),
    path('api/v1/auth/token/destroy/', TokenDestroyView.as_view())
]
