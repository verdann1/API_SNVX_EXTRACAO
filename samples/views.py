from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from samples.models import Sample
from samples.serializers import SamplesModelSerializer, SamplesListDetailSerializer, SamplesStatsSerializer
from products.models import Product

class SamplesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Sample.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SamplesListDetailSerializer
        return SamplesModelSerializer

class SamplesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Sample.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SamplesListDetailSerializer
        return SamplesModelSerializer

class SamplesStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Sample.objects.all()

    def get(self, request):
        # Corrigir agregações para usar 'assembly' (conforme o modelo real)
        total_samples = self.queryset.count()
        samples_by_assembly = self.queryset.values('assembly__name').annotate(
            count=Count('id')
        ).order_by('assembly__name')

        # Calcular total de produtos únicos associados a amostras
        total_products = Product.objects.filter(samples__isnull=False).distinct().count()

        # Formatar dados para o serializer
        formatted_data = {
            'total_samples': total_samples,
            'samples_by_assembly': [
                {
                    'assembly_name': item['assembly__name'],
                    'count': item['count']
                }
                for item in samples_by_assembly
            ],
            'total_products': total_products
        }

        # Validar e retornar
        serializer = SamplesStatsSerializer(data=formatted_data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
