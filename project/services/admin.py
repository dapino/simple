from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Skus, Subcategories, Categories, Groups, Services

class SkusResource(resources.ModelResource):
    class Meta:
        model = Skus

class SubcategoriesResource(resources.ModelResource):
    class Meta:
        model = Subcategories

class CategoriesResource(resources.ModelResource):
    class Meta:
        model = Categories

class GroupsResource(resources.ModelResource):
    class Meta:
        model = Groups

class ServicesResource(resources.ModelResource):
    class Meta:
        model = Services

@admin.register(Skus)
class SkusAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Skus
    resource_class = SkusResource
    search_fields = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']
    list_display = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']
    list_filter = ['Status']

@admin.register(Subcategories)
class SubcategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Subcategories
    resource_class = SubcategoriesResource
    search_fields = ['id', 'name',]
    list_display = ['id', 'name',]

@admin.register(Categories)
class CategoriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Categories
    resource_class = CategoriesResource
    search_fields = ['id', 'name',]
    list_display = ['id', 'name',]

@admin.register(Groups)
class GroupsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Groups
    resource_class = GroupsResource
    search_fields = ['id', 'name',]
    list_display = ['id', 'name',]

@admin.register(Services)
class ServicesAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = Services
    resource_class = ServicesResource
    search_fields = ['id', 'idgroups', 'idcategories', 'idsubcategories', 'idskus',]
    list_display = ['id', 'idgroups', 'idcategories', 'idsubcategories', 'idskus',]




