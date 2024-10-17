from django.urls import path, include
from rest_framework.routers import DefaultRouter
from my_app.views import CityViewSet, StreetViewSet, ShopViewSet

router = DefaultRouter()
router.register(r'city', CityViewSet)
router.register(r'street', StreetViewSet)
router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('city/<int:city_id>/street/', StreetViewSet.as_view({'get': 'list'}), name='city-street-list'),
]
