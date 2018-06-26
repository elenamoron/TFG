from rest_framework import serializers
from client.models import LegalPerson, PhysicalPerson, Document, SupportDoc
from organization.models import Project


class LegalPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = LegalPerson
        fields = ('id', 'project_id', 'denominacion_social', 'CIF', 'ubicacion', 'fecha_constitucion', 'sector',
                  'forma_juridica', 'registro', 'numero_inscripciones', 'poblacion', 'provincia', 'codigo_postal',
                  'pais', 'telefono', 'email')


class PhysicalPersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = PhysicalPerson
        fields = ('id', 'project_id', 'nombre_completo', 'documento_identificativo', 'fecha_caducidad', 'nacionalidad',
                  'pais_nacionalidad', 'lugar_nacimiento', 'pais_residencia', 'domicilio', 'telefono', 'email',
                  'capital', 'responsabilidad_publica', 'controla_sociedad', 'control')


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('content_type', 'length', 'file')


class SupportSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all())
    persona_juridica = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                                          queryset=LegalPerson.objects.all())
    persona_fisica = serializers.PrimaryKeyRelatedField(required=False, many=False,
                                                        queryset=PhysicalPerson.objects.all())

    class Meta:
        model = SupportDoc
        fields = ('project', 'persona_juridica', 'persona_fisica', 'cod_justificacion')

