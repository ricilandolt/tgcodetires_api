from rest_framework import serializers
from tgcode.models import TgCode
from tire.serializers import TireSerializer
from rim.serializers import RimSerializer

class TgCodeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TgCode
        fields = '__all__' 

    def to_representation(self, instance):
        representation = super().to_representation(instance) 
        representation['tires'] = TireSerializer(instance.tires, many = True).data
        representation['rims'] = RimSerializer(instance.rims, many = True).data
        return representation