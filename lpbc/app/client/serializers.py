from rest_framework import serializers
from client.models import LegalPerson

class LegalPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalPerson
        fields = ('denominacion_social', 'CIF', 'ubicacion', 'fecha_constitucion', 'sector', 'forma_juridica',
                  'registro', 'numero_inscripciones', 'poblacion', 'provincia', 'codigo_postal', 'pais', 'telefono',
                  'email')
