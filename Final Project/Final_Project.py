class Recipe1:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def cooking_time(self):
        print(f"{self.name} should be cooked for 30 minutes.")

class Recipe2:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def cooking_time(self):
        print(f"{self.name} should be cooked for 20 minutes.")

class Recipe3:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def cooking_time(self):
        print(f"{self.name} should be cooked for 40 minutes.")

recipe1 = Recipe1("Spaghetti Bolognese", ["Spaghetti", "Tomato Sauce", "Beef", "Onion", "Garlic"])
recipe2 = Recipe2("Caesar Salad", ["Lettuce", "Chicken", "Croutons", "Parmesan", "Caesar Dressing"])
recipe3 = Recipe3("Chocolate Cake", ["Flour", "Cocoa", "Sugar", "Butter", "Eggs"])

print(f"\nRecipe 1: {recipe1.name}")
print("Ingredients:", ', '.join(recipe1.ingredients))
recipe1.cooking_time()

print(f"\nRecipe 2: {recipe2.name}")
print("Ingredients:", ', '.join(recipe2.ingredients))
recipe2.cooking_time()

print(f"\nRecipe 3: {recipe3.name}")
print("Ingredients:", ', '.join(recipe3.ingredients))
recipe3.cooking_time()
