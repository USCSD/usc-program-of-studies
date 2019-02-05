from rest_framework import serializers
from api.models import Class,Career,Info


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'code', 'class_name', 'credits', 'length', 'weighted',
                  'subject', 'grade', 'qualification', 'careers', 'description', 'link','mods')

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id','career_name','description','career_pathways','suggested_classes')

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id','info_name','file_name')
