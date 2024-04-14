from django.shortcuts import render
from rest_framework import serializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apartments.models import Apartment, Client
from apartments.serializers import ApartmentSerializerValidator

# Create your views here.
class ApartmentListAPIView(ListCreateAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializerValidator
    pagination_class = None


class ApartmentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializerValidator
    lookup_field = "id"



class ClientListAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ModelSerializer
    pagination_class = None


class ClientDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ModelSerializer
    lookup_field = "id"

