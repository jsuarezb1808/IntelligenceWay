from .models import LearningMethods
from rest_framework import serializers

#se utiliza para convertir los datos a un Json
class LearningMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model= LearningMethods
        fields = '__all__'
        
