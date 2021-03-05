from django.http import HttpResponseRedirect
from .models import RecipesItem, IngredientsItem, EquipmentItem
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Views
@login_required
# def home(request):
#     return render(request, "registration/success.html", {})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # return redirect('home')
            return redirect('recipes_view')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def recipes_view(request):
    all_recipes = RecipesItem.objects.all()
    return render(request, 'recipes.html',
                  {'all_items': all_recipes})


def relevant_recipes_view(request):
    all_recipes = RecipesItem.objects.all()
    ingredients_objects = IngredientsItem.objects.all()
    equipment_objects = EquipmentItem.objects.all()
    relevant_recipes = []
    # ingredients = []
    # for ingredient in ingredients_objects:
    #     ingredients.append(ingredient.content)
    ingredients = [ingredient.content for ingredient in ingredients_objects]
    equipment = [item.content for item in equipment_objects]
    print('ingredients: ', ingredients)
    for recipe in all_recipes:
        counter = 0
        ingredients_list = recipe.content.split('ingredients: ')
        # print('l: ', l)
        equipment_list = recipe.content.split('equipment: ')
        if len(ingredients_list) > 1:
            recipe_ingredients = ingredients_list[1].split(',')
        else:
            recipe_ingredients = []
        if len(equipment_list) > 1:
            recipe_equipment = equipment_list[1].split(',')
        else:
            recipe_equipment = []
        # print('recipe ingredients: ', recipe_ingredients)
        for ingredient in recipe_ingredients:
            # print('ingredient: ', ingredient)
            if ingredient not in ingredients:
                # print('if1')
                counter = counter + 1
                if counter > 2:
                    # print('if2')
                    break
        if counter <= 2:
            # print('if3')
            for item in recipe_equipment:
                counter = 0
                if item not in equipment:
                    counter = counter + 1
                    if counter > 1:
                        break
            if counter <= 1:
                relevant_recipes.append(recipe)
    # return render(request, 'recipes.html',
    #               {'all_items': all_recipes})
    return render(request, 'recipes.html',
                  {'all_items': relevant_recipes})


def add_recipe_view(request):
    x = request.POST['content']
    new_item = RecipesItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/allrecipes/')


def delete_recipe_view(request, i):
    y = RecipesItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/allrecipes/')


def ingredients_view(request):
    all_ingredients = IngredientsItem.objects.all()
    return render(request, 'ingredients.html',
                  {'all_items': all_ingredients})


def add_ingredient_view(request):
    x = request.POST['content']
    new_item = IngredientsItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/ingredients/')


def delete_ingredient_view(request, i):
    y = IngredientsItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/ingredients/')


def equipment_view(request):
    all_equipment = EquipmentItem.objects.all()
    return render(request, 'equipment.html',
                  {'all_items': all_equipment})


def add_equipment_view(request):
    x = request.POST['content']
    new_item = EquipmentItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/equipment/')


def delete_equipment_view(request, i):
    y = EquipmentItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/equipment/')
