from django.urls import path
from myapp.views import recipe_views as views

app_name = "recipes"

urlpatterns = [
    
    # 🌐 Rutas HTML
    path("", views.list_recipes, name="list_recipes"),
    path("create/", views.create_recipe, name="create_recipe"),
    path("edit/<int:recipe_id>/", views.edit_recipe, name="edit_recipe"),
    path("delete/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
    
    # 🧩 Endpoints JSON tipo API
    path("json/", views.index, name="index_api"),
    path("json/<int:recipe_id>/", views.get_one_recipe, name="get_one_recipe_api"),
]
