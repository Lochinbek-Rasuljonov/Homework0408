from rest_framework import serializers
from .models import Branch, Category_FastFood, FastFood



class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        exclude = ('added_time',)


class Category_FastFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_FastFood
        exclude = ('added_time',)


class FastFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FastFood
        exclude = ('added_time',)