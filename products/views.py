from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from products.serializers import ProductSerializer
from app.permissions import GlobalDefaultPermission


class ProductCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
