from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Cliente, TipoPropiedad, Propiedad, Contrato, ContratoEstado
from .serializers import ClienteSerializer, TipoPropiedadSerializer, PropiedadSerializer
from .serializers import ContratoSerializer, ContratoEstadoSerializer

from rest_framework import viewsets, mixins, generics

def home(request):
    return HttpResponse("Estas en la seccion del Modulo 1")

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by()
    serializer_class = ClienteSerializer

class TipoPropiedadViewSet(viewsets.ModelViewSet):
    queryset = TipoPropiedad.objects.all().order_by()
    serializer_class = TipoPropiedadSerializer

class PropiedadViewSet(viewsets.ModelViewSet):
    queryset = Propiedad.objects.all().order_by()
    serializer_class = PropiedadSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all().order_by()
    serializer_class = ContratoSerializer

class ContratoEstadoViewSet(viewsets.ModelViewSet):
    queryset = ContratoEstado.objects.all().order_by()
    serializer_class = ContratoEstadoSerializer