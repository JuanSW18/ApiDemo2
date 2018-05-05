from rest_framework import serializers
from .models import Cliente, TipoPropiedad, Propiedad, Contrato, ContratoEstado

# campos que se van a mostrar
class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre_cliente', 'apellido_cliente', 'telefono_cliente')

class TipoPropiedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPropiedad
        fields = ('__all__')

class PropiedadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Propiedad
        fields = ('id_propiedad', 'id_tipoPropiedad', 'num_habitacion')

class ContratoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contrato
        fields = ('__all__')

class ContratoEstadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContratoEstado
        fields = ('estado', )