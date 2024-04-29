from rest_framework import serializers

from apps.products.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productfields = ('id', 'title',
        'description', 'price', 'image')