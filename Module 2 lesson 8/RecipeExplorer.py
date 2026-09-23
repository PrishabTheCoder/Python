pasta = ("pasta arrabiata", "italian", 20, "medium")
biryani = ("chicken biryani", "indian", 45, "hard")
print("Recipe 1", pasta)
print ("name", pasta[0])
print("cuisine",pasta[1])
print("difficulty:", pasta[1])

all_recipes = (pasta, biryani)
print("\nfirst recipe name:", all_recipes[0][0])
print("second recipe time:", all_recipes[1][2], "mins")
print("Pasta details (sliced):", pasta[1:3])

print ("\npasta recipe details:")
for details in pasta:
    print("-",details)

pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"} 
print("\npasta ingredients:", pasta_ingredients)
print("Biryani ingredients:", biryani_ingredients)
print("total pasta ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("common ingredients (intersection):", common)
print("only in pasta (difference):",only_pasta)
print("not shared (sym. difference):", unique_to_each) 