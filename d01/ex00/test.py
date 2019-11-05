from recipe import Recipe
from book import Book

#tourte =  Recipe("", 1, 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("cookies", 11, 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("cookies", "s", 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("jk", 1, 63, ["fdfd", 1], "", "lunch")
tourte =  Recipe("jk", 1, 63, ["fdfd", "1"], "", "lunch")
cookies =  Recipe("cookies", 1, 63, ["beurre", "farine"], "", "lunch")
toPrint = str(tourte)
print(toPrint)

annuaire = Book()
annuaire.add_recipe(cookies)
annuaire.add_recipe(tourte)
annuaire.get_recipes_by_types("lunch")
annuaire.get_recipe_by_name("jk")




