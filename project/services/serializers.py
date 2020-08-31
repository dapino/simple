from rest_framework import serializers
from services.models import Skus, Subcategories, Categories, Groups, Services


class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ['idskus', 'group','category', 'subcategory', 'sku', 'sku_description', 'sku_specification', 'sku_price', 'sku_time']
    
    group = serializers.SerializerMethodField('get_group_name')
    category = serializers.SerializerMethodField('get_category_name')
    subcategory = serializers.SerializerMethodField('get_subcategory_name')
    sku = serializers.SerializerMethodField('get_sku_name')
    sku_description = serializers.SerializerMethodField('get_sku_description')
    sku_specification = serializers.SerializerMethodField('get_sku_specification')
    sku_price = serializers.SerializerMethodField('get_sku_price')
    sku_time = serializers.SerializerMethodField('get_sku_time')

    def get_group_name(self, obj):
        return obj.idgroups.name

    def get_category_name(self, obj):
        return obj.idcategories.name
    
    def get_subcategory_name(self, obj):
        return obj.idsubcategories.name
    
    def get_sku_name(self, obj):
        return obj.idskus.name
    
    def get_sku_description(self, obj):
        return obj.idskus.description
    
    def get_sku_specification(self, obj):
        return obj.idskus.specification
    
    def get_sku_price(self, obj):
        return obj.idskus.price

    def get_sku_time(self, obj):
        return obj.idskus.time_stimated