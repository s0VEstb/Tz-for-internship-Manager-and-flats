from rest_framework import serializers, validators
from .models import Apartment, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ApartmentSerializerValidator(serializers.ModelSerializer):
    square = serializers.IntegerField(min_value=0)
    price = serializers.IntegerField(min_value=0)
    floor = serializers.IntegerField(min_value=0)
    client = ClientSerializer(read_only=True)

    class Meta:
        model = Apartment
        fields = ['id', 'object', 'floor', 'square', 'data', 'status', 'price', 'client']
