# myapp/views/recipe_views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .. import models
from ..forms import RecipeForm
from django.core.exceptions import ObjectDoesNotExist
import json


# 🔹 Mostrar todas las recetas (JSON)
def index(request):
    all_recipes = models.Recipes.objects.all().values()
    return JsonResponse(
        list(all_recipes), safe=False, json_dumps_params={"ensure_ascii": False}
    )


# 🔹 Mostrar una receta por ID (JSON)
def get_one_recipe(request, recipe_id):
    try:
        one_recipe = models.Recipes.objects.get(id=recipe_id)
        return JsonResponse(
            {
                "id": one_recipe.id,
                "name": one_recipe.name,
                "ingredients": one_recipe.ingredients,
                "preparation": one_recipe.preparation,
                "people": one_recipe.people,
                "onMenu": one_recipe.onMenu,
            },
            json_dumps_params={"ensure_ascii": False},
        )
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Recipe not found"}, status=404)


# 🔹 Crear receta (formulario HTML y POST)
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("recipes:index")
    else:
        form = RecipeForm()
    return render(request, "recipes/create_recipe.html", {"form": form})


# 🔹 Editar receta
def edit_recipe(request, recipe_id):
    recipe = models.Recipes.objects.get(id=recipe_id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipes:index")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/edit_recipe.html", {"form": form})


# 🔹 Eliminar receta
def delete_recipe(request, recipe_id):
    recipe = models.Recipes.objects.get(id=recipe_id)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipes:index")
    return render(request, "recipes/delete_recipe.html", {"recipe": recipe})
