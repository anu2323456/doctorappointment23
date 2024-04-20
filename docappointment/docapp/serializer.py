from rest_framework import serializers
from .models import *

class DocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'


class DocappontmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docappontment
        fields = ['time', 'date', 'Patientname','doctor']




