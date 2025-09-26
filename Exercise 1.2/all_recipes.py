# all_recipes.py
# Exercise 1.2 - Task
# This script creates five recipe structures and stores them in an outer structure.

# Recipe 1
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

# Recipe 2
recipe_2 = {
    "name": "Pancakes",
    "cooking_time": 15,
    "ingredients": ["Flour", "Eggs", "Milk", "Sugar", "Butter"]
}

# Recipe 3
recipe_3 = {
    "name": "Salad",
    "cooking_time": 10,
    "ingredients": ["Lettuce", "Tomato", "Cucumber", "Olive oil"]
}

# Recipe 4
recipe_4 = {
    "name": "Grilled Cheese",
    "cooking_time": 7,
    "ingredients": ["Bread", "Cheese", "Butter"]
}

# Recipe 5
recipe_5 = {
    "name": "Omelette",
    "cooking_time": 6,
    "ingredients": ["Eggs", "Salt", "Pepper", "Cheese"]
}

# Outer structure to hold all recipes
all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

# Print the ingredients for each recipe
for recipe in all_recipes:
    print(f"{recipe['name']} ingredients: {recipe['ingredients']}")
