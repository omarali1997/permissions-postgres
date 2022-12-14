from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SweetSerializer

from .models import Snack

class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SweetSerializer

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SweetSerializer
