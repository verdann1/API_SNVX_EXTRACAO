from rest_framework import serializers
from .models import Sample
from assembly.serializers import AssemblySerializer
from products.serializers import ProductSerializer
from assembly.models import Assembly
from products.models import Product

class SamplesSerializer(serializers.ModelSerializer):
    """
    Serializer básico para operações de leitura/escrita simplificadas.
    """
    assembly = serializers.PrimaryKeyRelatedField(
        queryset=Assembly.objects.all()
    )
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True
    )

    class Meta:
        model = Sample
        fields = ['id', 'assembly', 'products', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class SamplesModelSerializer(serializers.ModelSerializer):
    """
    Serializer com validações específicas.
    """
    class Meta:
        model = Sample
        fields = ['id', 'assembly', 'products', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

    def validate_assembly(self, value):
        # Exemplo de validação customizada
        if not value.is_active:  # Assumindo que Assembly tenha um campo `is_active`
            raise serializers.ValidationError("O assembly selecionado está inativo.")
        return value

class SamplesListDetailSerializer(serializers.ModelSerializer):
    """
    Serializer detalhado com serialização aninhada para leitura.
    """
    assembly = AssemblySerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Sample
        fields = ['id', 'assembly', 'products', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']

class SamplesStatsSerializer(serializers.Serializer):
    total_samples = serializers.IntegerField()
    samples_by_assembly = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField(),
            allow_empty=True
        )
    )
    total_products = serializers.IntegerField()

class SampleCreateSerializer(serializers.ModelSerializer):
    """
    Serializer especializado para criação de amostras com produtos.
    """
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Sample
        fields = ['assembly', 'products']

    def create(self, validated_data):
        products = validated_data.pop('products')
        sample = super().create(validated_data)
        sample.products.set(products)
        return sample