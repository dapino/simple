from django.contrib import admin
from .models import Skus, Subcategories, Categories, Groups, Services

@admin.register(Skus)
class SkusAdmin(admin.ModelAdmin):
    model = Skus
    search_fields = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']
    list_display = ['id', 'name', 'description', 'specification', 'price', 'time_stimated', 'Status']
    list_filter = ['Status']


