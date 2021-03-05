from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
# from easy_chef_app.views import easy_chef_app_view, add_easy_chef_view, delete_easy_chef_view, home, register
from easy_chef_app.views import recipes_view, add_recipe_view, delete_recipe_view, register, ingredients_view, \
    add_ingredient_view, delete_ingredient_view, relevant_recipes_view, equipment_view, add_equipment_view, \
    delete_equipment_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('allrecipes/', recipes_view),
    path('relevantrecipes/', relevant_recipes_view),
    path('addrecipesitem/', add_recipe_view),
    path('deleterecipesitem/<int:i>/', delete_recipe_view),
    path('ingredients/', ingredients_view),
    path('addingredientsitem/', add_ingredient_view),
    path('deleteingredientsitem/<int:i>/', delete_ingredient_view),
    path('equipment/', equipment_view),
    path('addequipmentitem/', add_equipment_view),
    path('deleteequipmentitem/<int:i>/', delete_equipment_view),
]
