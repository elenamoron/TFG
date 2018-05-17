from rest_framework import serializers
from client.models import LegalPerson, PhysicalPerson, Document
from organization.models import Project


class LegalPersonSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all())

    class Meta:
        model = LegalPerson
        fields = ('id', 'project', 'denominacion_social', 'CIF', 'ubicacion', 'fecha_constitucion', 'sector',
                  'forma_juridica', 'registro', 'numero_inscripciones', 'poblacion', 'provincia', 'codigo_postal',
                  'pais', 'telefono', 'email')


class PhysicalPersonSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False,  queryset=Project.objects.all())

    class Meta:
        model = PhysicalPerson
        fields = ('id', 'project', 'nombre_completo', 'documento_identificativo', 'fecha_caducidad', 'nacionalidad',
                  'pais_nacionalidad', 'lugar_nacimiento', 'pais_residencia', 'domicilio', 'telefono', 'email',
                  'capital', 'responsabilidad_publica', 'controla_sociedad', 'control')


class FileSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all())
    persona_juridica = serializers.PrimaryKeyRelatedField(many=False, queryset=LegalPerson.objects.all())

    class Meta:
        model = Document
        fields = ('meta_descripcion', 'file', 'project', 'persona_juridica')
