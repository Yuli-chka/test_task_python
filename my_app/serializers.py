from rest_framework import serializers
from my_app.models import City, Street, Shop

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ['id', 'name', 'city']

class ShopSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    street_name = serializers.CharField(source='street.name', read_only=True)

    class Meta:
        model = Shop
        fields = ['id', 'name', 'city_name', 'street_name', 'city', 'street', 'house', 'opening_time', 'closing_time']