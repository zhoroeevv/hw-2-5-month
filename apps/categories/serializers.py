from rest_framework import serializers

from apps.categories.models import Category

class СategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'parent', 'slug')    
    