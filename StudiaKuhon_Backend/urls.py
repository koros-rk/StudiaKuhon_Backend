from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from disign_shop.views import *
from disign_shop.TelegramOrder import OrderView

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'styles', StyleViewSet, basename='style')
router.register(r'materials', MaterialViewSet, basename='materials')
router.register(r'palettes', PaletteViewSet, basename='palettes')
router.register(r'photos', PhotoViewSet, basename='photos')
router.register(r'handles', HandleViewSet, basename='handles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/order', OrderView.as_view()),
    path('api/v1/products/gallery', ProductGallery.as_view()),
    path('api/v1/auth2', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
]
