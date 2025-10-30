from django.urls import path
from . import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.get_one_recipe, name="get_one_recipe"),
    path("create/", views.create_recipe, name="create_recipe"),
    path("edit/<int:recipe_id>/", views.edit_recipe, name="edit_recipe"),
    path("delete/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
]
