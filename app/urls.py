from django.urls import path
from .views import (Category_FastFoodListView, Category_FastFoodCreateView, Category_FastFoodListCreateView, Category_FastFoodRetrieveView,
                    FastFoodListView, FastFoodCreateView, FastFoodListCreateView, FastFoodRetrieveView,
                    BranchListView, BranchCreateView, BranchListCreateView, BranchRetrieveView)




urlpatterns = [
    path('', FastFoodListView.as_view()),
    path('fastfood-create/', FastFoodCreateView.as_view()),
    path('fastfood-list-create/', FastFoodListCreateView.as_view()),
    path('fastfood-retrieve/<int:pk>', FastFoodRetrieveView.as_view()),

    path('category-list/', Category_FastFoodListView.as_view()),
    path('category-create/', Category_FastFoodCreateView.as_view()),
    path('category-list-create/', Category_FastFoodListCreateView.as_view()),
    path('category-retrieve/<int:pk>', Category_FastFoodRetrieveView.as_view()),

    path('branch-list/', BranchListView.as_view()),
    path('branch-create/', BranchCreateView.as_view()),
    path('branch-list-create/', BranchListCreateView.as_view()),
    path('branch-retrieve/<int:pk>', BranchRetrieveView.as_view()),
]