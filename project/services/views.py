from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from services.models import Services
from services.serializers import ServicesSerializer

def simple_services(request):
    """
    List all skus.
    """
    if request.method == 'GET':
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many=True)
        return JsonResponse(serializer.data, safe=False)

