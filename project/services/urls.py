from django.urls import path, include
from services import views

urlpatterns = [
    path('services/', views.simple_services),
]