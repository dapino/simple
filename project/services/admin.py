from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.contrib import admin
from .models import Skus, Subcategories, Categories, Groups, Services

class SkusResource(resources.ModelResource):
    class Meta:
        model = Skus

@admin.register(Skus)
class SkusAdmin(ImportExportActionModelAdmin, admin.ModelAdmin):
    model = Skus
    resource_class = SkusResource
    search_fields = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']
    list_display = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']
    list_filter = ['Status']



