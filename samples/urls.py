from django.urls import path
from . import views

urlpatterns = [
    path('samples/', views.SamplesCreateListView.as_view(), name='sample-create-list'),
    path('samples/<int:pk>/', views.SamplesRetrieveUpdateDestroyView.as_view(), name='sample-detail-view'),
    path('samples/stats/', views.SamplesStatsView.as_view(), name='sample-stats-view'),
]
