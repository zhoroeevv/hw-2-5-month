from rest_framework.viewsets import ModelViewSet

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
