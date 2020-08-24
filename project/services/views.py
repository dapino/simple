from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from services.models import Skus
from services.serializers import SkusSerializer

def list_skus(request):
    """
    List all skus.
    """
    if request.method == 'GET':
        skus = Skus.objects.all()
        serializer = SkusSerializer(skus, many=True)
        return JsonResponse(serializer.data, safe=False)

