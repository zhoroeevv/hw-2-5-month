from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.categories.models import Category
from apps.categories.serializers import СategorySerializer

class CategoryViewSet(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = СategorySerializer

class CategoryDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = СategorySerializer