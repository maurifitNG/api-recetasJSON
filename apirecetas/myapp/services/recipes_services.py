from myapp.models import Recipes
from django.core.exceptions import ObjectDoesNotExist

def get_all_recipes():
    """Retorna todas las recetas."""
    return Recipes.objects.all()


def get_recipe_by_id(recipe_id):
    """Retorna una receta por su ID"""
    try:
        return Recipes.objects.get(id=recipe_id)
    except ObjectDoesNotExist:
        return None
    
    
def create_recipe(data):
    """Crea una receta nueva"""
    recipe = Recipes(**data)
    recipe.save()
    return recipe


def update_recipe(recipe_id, data):
    """Actualiza una receta existente"""
    recipe = get_recipe_by_id(recipe_id)
    if not recipe:
        return None
    for key, value in data.tiems():
        setattr(recipe, key, value)
    recipe.save()
    return recipe

def delete_recipe(recipe_id):
    """Elimina una receta por ID"""
    recipe = get_recipe_by_id(recipe_id)
    if recipe:
        recipe.delete()
        return True
    return False