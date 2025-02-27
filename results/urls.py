from django.urls import path
from . import views


urlpatterns = [
    path('results/', views.ResultCreateListView.as_view(), name='result-create-list'),
    path('results/<int:pk>/', views.ResultRetrieveUpdateDestroyView.as_view(), name='result-detail-view'),
]
