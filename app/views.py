from django.shortcuts import render
from rest_framework import generics
from .models import Branch, Category_FastFood, FastFood
from .serializers import BranchSerializer, Category_FastFoodSerializer, FastFoodSerializer

# Create your views here.


# CATEGORY_FASTFOOD
class Category_FastFoodListView(generics.ListAPIView):
    queryset = Category_FastFood.objects.all()
    serializer_class = Category_FastFoodSerializer

class Category_FastFoodCreateView(generics.CreateAPIView):
    queryset = Category_FastFood.objects.all()
    serializer_class = Category_FastFoodSerializer

class Category_FastFoodListCreateView(generics.ListCreateAPIView):
    queryset = Category_FastFood.objects.all()
    serializer_class = Category_FastFoodSerializer

class Category_FastFoodRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category_FastFood.objects.all()
    serializer_class = Category_FastFoodSerializer


# FASTFOOD
class FastFoodListView(generics.ListAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

class FastFoodCreateView(generics.CreateAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

class FastFoodListCreateView(generics.ListCreateAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer

class FastFoodRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FastFood.objects.all()
    serializer_class = FastFoodSerializer


# BRANCH
class BranchListView(generics.ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchCreateView(generics.CreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = FastFoodSerializer

class BranchListCreateView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer