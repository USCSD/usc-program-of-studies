from rest_framework import serializers
from api.models import Class,Career


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'code', 'class_name', 'credits', 'length', 'weighted',
                  'subject', 'grade', 'qualification', 'careers', 'description', 'link')

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ('id','career_name','description','career_pathways','suggested_classes')
