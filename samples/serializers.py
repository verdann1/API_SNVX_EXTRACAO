from django.db.models import Avg
from rest_framework import serializers
from products.serializers import ProductSerializer
from samples.models import Sample
from assembly.models import Assembly
from assembly.serializers import AssemblySerializer
from products.models import Product


class SamplesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Assembly.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        many=True,
    )
    resume = serializers.CharField()


class SamplesModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sample
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900.')
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('Resumo não deve ser maior do que 500 caracteres.')
        return value


class SamplesListDetailSerializer(serializers.ModelSerializer):
    actors = ProductSerializer(many=True)
    genre = AssemblySerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Sample
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if rate:
            return round(rate, 1)

        return None


class SamplesStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
