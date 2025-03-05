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
        # Usar 'assembly__id' em vez de 'assembly__name'
        samples_by_assembly = Sample.objects.values('assembly__id').annotate(
            count=Count('id')
        ).order_by('assembly__id')

        # Formatar dados
        data = {
            'total_samples': Sample.objects.count(),
            'samples_by_assembly': [
                {
                    'assembly_id': item['assembly__id'],  # Renomear para 'assembly_id'
                    'count': item['count']
                }
                for item in samples_by_assembly
            ],
            'total_products': Product.objects.filter(samples__isnull=False).distinct().count()
        }

        serializer = SamplesStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data)
