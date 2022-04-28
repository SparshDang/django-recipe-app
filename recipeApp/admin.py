from django.contrib import admin

from recipeApp.models import Recipe

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Recipe, RecipeAdmin)
