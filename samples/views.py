from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from samples.models import Sample
from samples.serializers import SamplesModelSerializer, SamplesListDetailSerializer, SamplesStatsSerializer
from results.models import Result


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
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        total_reviews = Result.objects.count()
        average_stars = Result.objects.aggregate(avg_stars=Avg('stars'))['avg_stars']

        data = {
            'total_movies': total_movies,
            'movies_by_genre': movies_by_genre,
            'total_reviews': total_reviews,
            'average_stars': round(average_stars, 1) if average_stars else 0,
        }
        serializer = SamplesStatsSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        return response.Response(
            data=serializer.validated_data,
            status=status.HTTP_200_OK,
        )
