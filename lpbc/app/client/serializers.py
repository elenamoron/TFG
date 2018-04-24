from rest_framework import serializers
from client.models import LegalPerson, PhysicalPerson
from organization.models import Project


class LegalPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalPerson
        fields = ('denominacion_social', 'CIF', 'ubicacion', 'fecha_constitucion', 'sector',
                  'forma_juridica', 'registro', 'numero_inscripciones', 'poblacion', 'provincia', 'codigo_postal',
                  'pais', 'telefono', 'email')


class PhysicalPersonSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False,  queryset=Project.objects.all())

    class Meta:
        model = PhysicalPerson
        fields = ('id', 'project', 'nombre_completo', 'documento_identificativo', 'fecha_caducidad', 'nacionalidad',
                  'pais_nacionalidad', 'lugar_nacimiento', 'pais_residencia', 'domicilio', 'telefono', 'email',
                  'acreditacion_poderes')
