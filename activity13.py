pasta=("pasta arrabiata", "italian", 20, "medium")
biryani=("chicken biryani","indian",45,"hard")
print("recipe 1:",pasta)
print("name:",pasta[0])
print("cusine:",pasta[1])
print("difficulty:",pasta[-1])

all_recipes=(pasta,biryani)
print("\nFirst recipe name:", all_recipes[0][0])
print("second recipe time:", all_recipes[1][2],"mins")
print("pasta details (sliced):", pasta[1:3])

print("\nPasta recipe details:")
for details in pasta:
    print("-",details)

    pasta_ingredients = {"tomato","garlic","olive oil","chilli","pasta","garlic"}
    biryani_ingredients = {"rice","chicken","garlic","onion","tomato","spices"}
    print("\nPasta ingredients:",pasta_ingredients)
    print("biryani ingredients:",biryani_ingredients)
    print("total pasta ingredients:",len(pasta_ingredients))

    pasta_ingredients.add("pamesan")
    pasta_ingredients.discard("chilli")
    print("\nUpdated pasta ingredients:",pasta_ingredients)

    all_ingredients=pasta_ingredients.union(biryani_ingredients)
    common=pasta_ingredients.intersection(biryani_ingredients)
    only_pasta=pasta_ingredients.difference(biryani_ingredients)
    uniques_to_each=pasta_ingredients.symmetric_difference(biryani_ingredients)

    print("\nAll ingredients (union):", all_ingredients)
    print("common ingredients(intersection):",common)
    print("only in pasta (diffrence):",only_pasta)
    print("Not shared(sym.diffrence):",uniques_to_each)