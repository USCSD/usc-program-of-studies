from rest_framework import serializers
from api.models import Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ('id', 'code', 'class_name', 'credits', 'length', 'weighted',
                  'subject', 'grade', 'qualification', 'career', 'description', 'link')
