from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission
from assembly.models import Assembly
from assembly.serializers import AssemblySerializer


class AssemblyCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer


class AssemblyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Assembly.objects.all()
    serializer_class = AssemblySerializer
