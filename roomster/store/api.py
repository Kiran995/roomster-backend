from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from store.models import Space, Facility, Furniture
from store.serializers import SpaceSerializer, FurnitureSerializer

class SpaceAPIViewset(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Space.objects.all()
    serializer_class = SpaceSerializer
    filter_backends = (DjangoFilterBackend,)

class FurnitureAPIViewset(viewsets.ModelViewSet):
    permission_classes = []
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer
    filter_backends = (DjangoFilterBackend,)