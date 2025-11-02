# myapp/views/recipe_views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from myapp.forms import RecipeForm
from myapp.services import recipes_services


# 🔹 Listar todas las recetas (HTML)
def list_recipes(request):
    recipes = recipes_services.get_all_recipes()
    return render(request, "recipes/list_recipes.html", {"recipes": recipes})


# 🔹 Mostrar todas las recetas (JSON)
def index(request):
    all_recipes = recipes_services.get_all_recipes().values()
    return JsonResponse(
        list(all_recipes), safe=False, json_dumps_params={"ensure_ascii": False}
    )


# 🔹 Mostrar una receta por ID (JSON)
def get_one_recipe(request, recipe_id):
    recipe = recipes_services.get_recipe_by_id(recipe_id)
    if not recipe:
        return JsonResponse({"error": "Recipe not found"}, status=404)
    return JsonResponse(
        {
            "id": recipe.id,
            "name": recipe.name,
            "ingredients": recipe.ingredients,
            "preparation": recipe.preparation,
            "people": recipe.people,
            "onMenu": recipe.onMenu,
        },
        json_dumps_params={"ensure_ascii": False},
    )


# 🔹 Crear receta
def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipes_services.create_recipe(form.cleaned_data)
            messages.success(request, "Receta creada exitosamente 🍳")
            return redirect("recipes:list_recipes")
        else:
            messages.error(request, "Error al crear la receta. Verifica los datos.")
    else:
        form = RecipeForm()
    return render(request, "recipes/create_recipe.html", {"form": form})


# 🔹 Editar receta
def edit_recipe(request, recipe_id):
    recipe = recipes_services.get_recipe_by_id(recipe_id)
    if not recipe:
        messages.error(request, "La receta no existe.")
        return redirect("recipes:list_recipes")

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, "Receta actualizada correctamente ✏️")
            return redirect("recipes:list_recipes")
        else:
            messages.error(request, "Error al actualizar la receta.")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "recipes/edit_recipe.html", {"form": form})


# 🔹 Eliminar receta
def delete_recipe(request, recipe_id):
    recipe = recipes_services.get_recipe_by_id(recipe_id)
    if not recipe:
        messages.error(request, "La receta no existe o ya fue eliminada.")
        return redirect("recipes:list_recipes")

    if request.method == "POST":
        recipes_services.delete_recipe(recipe_id)
        messages.success(request, "Receta eliminada correctamente 🗑️")
        return redirect("recipes:list_recipes")
    return render(request, "recipes/delete_recipe.html", {"recipe": recipe})



