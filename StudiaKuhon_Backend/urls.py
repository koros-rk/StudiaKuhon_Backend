from django.contrib import admin
from djoser.views import TokenCreateView, TokenDestroyView
from django.urls import path, include, re_path
from rest_framework import routers

from disign_shop.views import *
from disign_shop.TelegramOrder import OrderView
from furniture_shop.views import *

router = routers.DefaultRouter()

# Design shop
router.register(r'design', ProductViewSet, basename='products')
router.register(r'design/styles', StyleViewSet, basename='style')
router.register(r'design/materials', MaterialViewSet, basename='materials')
router.register(r'design/palettes', PaletteViewSet, basename='palettes')
router.register(r'design/photos', PhotoViewSet, basename='photos')
router.register(r'design/handles', HandleViewSet, basename='handles')

# Furniture shop
router.register(r'furniture', FurnitureViewSet, basename='furniture')
router.register(r'furniture/categories', CategoryViewSet, basename='categories')
router.register(r'furniture/photos', FurniturePhotoViewSet, basename='photos')
router.register(r'furniture/colors', FurnitureColorViewSet, basename='colors')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/order', OrderView.as_view()),
    path('api/v1/auth', include('rest_framework.urls')),
    path('api/v1/auth/token/create/', TokenCreateView.as_view()),
    path('api/v1/auth/token/destroy/', TokenDestroyView.as_view())
]
