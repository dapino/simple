from django.urls import path, include
from services import views

urlpatterns = [
    path('skus/', views.list_skus),
]