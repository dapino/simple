from rest_framework import serializers
from services.models import Skus, Subcategories, Categories, Groups, Services

class SkusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skus
        fields = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']