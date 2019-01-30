from store.models import Space, Facility, Furniture
from rest_framework import serializers

class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields= '__all__'

class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'

