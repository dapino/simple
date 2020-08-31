from rest_framework import serializers
from services.models import Skus, Subcategories, Categories, Groups, Services


class ServicesSerializer(serializers.ModelSerializer):

    name_groups= Groups.name
    name_categories = Categories.name
    name_subcategories = Subcategories.name
    name_skus = Skus.name
    
    class Meta:
        model = Services
        fields = ['id', 'name_groups', 'name_category', 'name_subcategory', 'name_skus',]