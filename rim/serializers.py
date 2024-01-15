from rest_framework import serializers
from rim.models import Rim

class RimSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Rim
        fields = '__all__' 