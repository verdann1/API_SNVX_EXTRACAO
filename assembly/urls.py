from django.urls import path
from . import views


urlpatterns = [
    path('assembly/', views.AssemblyCreateListView.as_view(), name='assembly-create-list'),
    path('assembly/<int:pk>/', views.AssemblyRetrieveUpdateDestroyView.as_view(), name='assembly-detail-view'),
]
