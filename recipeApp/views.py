from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from recipeApp.models import Recipe

# Create your views here.


def recipeList(request):
    return render(request, 'recipeApp/index.html')


class RecipeListView(ListView):
    template_name = 'recipeApp/index.html'
    model = Recipe

    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    template_name = 'recipeApp/recipeDetail.html'
    model = Recipe
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        favorites = self.request.session.get('favourite')

        if favorites == None:
            context['isFavorite'] = False
        if self.object.id in favorites:
            context['isFavorite'] = True
        else:
            context['isFavorite'] = False

        return context


class FavouriteView(View):
    def post(self, request):
        recipeSlug = request.POST['recipeSlug']
        recipeId = Recipe.objects.get(slug=recipeSlug).id

        favourites = request.session.get('favourite')

        if favourites == None:
            favourites = [recipeId]
        elif recipeId not in favourites:
            favourites.append(recipeId)
        elif recipeId in favourites:
            favourites.remove(recipeId)

        request.session['favourite'] = favourites

        return HttpResponseRedirect(reverse('recipe', args=[recipeSlug]))

    def get(self, request):
        favourites = request.session.get('favourite')

        if favourites == None:
            favourites = []

        recipes = Recipe.objects.filter(id__in=favourites)

        return render(request, 'recipeApp/favorites.html', {
            'favourite': favourites,
            "recipes": recipes

        })
