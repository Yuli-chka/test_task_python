from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from my_app.models import City, Street, Shop
from my_app.serializers import CitySerializer, StreetSerializer, ShopSerializer
from django.utils import timezone
from rest_framework.decorators import api_view

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class StreetViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StreetSerializer
    queryset = Street.objects.all()

    def get_queryset(self):
        city_id = self.kwargs.get('city_id')
        if city_id:
            return Street.objects.filter(city_id=city_id)
        return Street.objects.all()

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def list(self, request):
        queryset = self.queryset

        # Фильтрация по параметрам
        street_id = request.query_params.get('street', None)
        city_id = request.query_params.get('city', None)
        open_status = request.query_params.get('open', None)

        if street_id:
            queryset = queryset.filter(street_id=street_id)
        if city_id:
            queryset = queryset.filter(city_id=city_id)
        if open_status is not None:
            current_time = timezone.now().time()
            if open_status == '1':
                queryset = queryset.filter(opening_time__lte=current_time, closing_time__gte=current_time)
            elif open_status == '0':
                queryset = queryset.exclude(opening_time__lte=current_time, closing_time__gte=current_time)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_streets_by_city(request, city_id):
    try:
        streets = Street.objects.filter(city_id=city_id)
        serializer = StreetSerializer(streets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except City.DoesNotExist:
        return Response({'error': 'City not found'}, status=status.HTTP_400_BAD_REQUEST)
