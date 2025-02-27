from rest_framework import serializers
from assembly.models import Assembly


class AssemblySerializer(serializers.ModelSerializer):

    class Meta:
        model = Assembly
        fields = '__all__'
