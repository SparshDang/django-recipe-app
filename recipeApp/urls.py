from django.urls import path

from recipeApp import views

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes-list'),
    path('recipe/<slug:slug>', views.RecipeDetailView.as_view(), name='recipe'),
    path('favorite/', views.FavouriteView.as_view(), name='favorite'),
]
