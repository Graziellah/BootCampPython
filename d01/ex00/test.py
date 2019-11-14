from recipe import Recipe
from book import Book

#tourte =  Recipe("", 1, 63, ["fdfd", "fjdskf"], "", "lunch")
try:
    tourte =  Recipe("cookies", 11, 63, ["fdfd", "fjdskf"], "", "lunch")
except ValueError as err:
    print(err)

print(tourte.cooking_level)
print(tourte.name)
#tourte =  Recipe("cookies", "s", 63, ["fdfd", "fjdskf"], "", "lunch")
#tourte =  Recipe("jk", 1, 63, ["fdfd", 1], "", "lunch")
#tourte =  Recipe("jk", 1, 63, ["fdfd", "1"], "", "lunch")
#cookies =  Recipe("cookies", 1, 63, ["beurre", "farine"], "", "lunch")
#toPrint = str(tourte)
#print(toPrint)

#annuaire = Book()
#print(annuaire.creation_date)
#annuaire.add_recipe(cookies)
#try:
#    annuaire.add_recipe("cake")
#except ValueError as err:
#    print("err", err)
#print(annuaire.last_update)
#annuaire.add_recipe(tourte)
#print(annuaire.last_update)
#annuaire.get_recipes_by_types("lunch")
#print(annuaire.last_update)
#annuaire.get_recipe_by_name("jk")



class Alphabet: 
    def __init__(self, value): 
        self._value = value 
          
    # getting the values     
    @property
    def value(self): 
        print('Getting value') 
        return self._value 
          
    # setting the values     
    @value.setter 
    def value(self, value): 
        self._value = value 
          
    # deleting the values 
    @value.deleter 
    def value(self): 
        del self._value 
  
  
# passing the value 
x = Alphabet('Peter')   
x.value = 'Diesel'
del x.value 

