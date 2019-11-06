from recipe import Recipe
from book import Book
import time


#tourte =  Recipe("", 1, 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("cookies", 11, 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("cookies", "s", 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("jk", 1, 63, ["fdfd", 1], "", "lunch")
tourte =  Recipe("jk", 1, 63, ["fdfd", "1"], "", "lunch")
cookies =  Recipe("cookies", 1, 63, ["beurre", "farine"], "", "lunch")
toPrint = str(tourte)
print(toPrint)

annuaire = Book()
print(annuaire.creation_date)
annuaire.add_recipe(cookies)
print(annuaire.last_update)
for i in range(0, 5000):
    a =  "b"
annuaire.add_recipe(tourte)
print(annuaire.last_update)
annuaire.get_recipes_by_types("lunch")
print(annuaire.last_update)
annuaire.get_recipe_by_name("jk")





