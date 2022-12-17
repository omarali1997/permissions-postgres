from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import SweetSerializer,PostSerializer
from .models import Snack,Post
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly


class SnackListView(ListCreateAPIView):
    queryset = Snack.objects.all()
    serializer_class = SweetSerializer

class SnackDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Snack.objects.all()
    serializer_class = SweetSerializer
    Permission_classes=[IsOwnerOrReadOnly]

class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes=[AllowAny]

class PostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    Permission_classes=[IsAuthenticatedOrReadOnly]
