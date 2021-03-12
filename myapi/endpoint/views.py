from django.shortcuts import render
from rest_framework import viewsets
#Se importa para permitir get, post, put and patch
from rest_framework.mixins import (CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin) 
from .serializers import ReviewsSerializer, PropertyTypesSerializer, StatesSerializer, CategoriesSerializer, CitiesSerializer, PropertiesSerializer, TransactionSerializer
from .models import Reviews, PropertyTypes, States, Cities, Categories, Properties, Transaction
# Create your views here.

class ReviewsViewSet(viewsets.GenericViewSet,CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Reviews.objects.all().order_by('id')
    serializer_class = ReviewsSerializer

class PropertyTypesViewSet(viewsets.GenericViewSet,CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = PropertyTypes.objects.all().order_by('id')
    serializer_class = PropertyTypesSerializer

class StatesViewSet(viewsets.GenericViewSet,CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = States.objects.all().order_by('id')
    serializer_class = StatesSerializer

class CitiesViewSet(viewsets.GenericViewSet,CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Cities.objects.all().order_by('id')
    serializer_class = CitiesSerializer

class CategoriesViewSet(viewsets.GenericViewSet,CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Categories.objects.all().order_by('id')
    serializer_class = CategoriesSerializer

class PropertiesViewSet(viewsets.GenericViewSet,CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    queryset = Properties.objects.all().order_by('id')
    serializer_class = PropertiesSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Properties.objects.all() 
    serializer_class = TransactionSerializer