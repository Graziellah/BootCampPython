from recipe import Recipe


class Book:
    def __init__(self):
        self.name = ""
        self.last_update = ""
        self.creation_date = ""
        self.recipes_list = {
            "starter": {},
            "lunch": {},
            "dessert": {}
        }

    def get_recipe_by_name(self, name):
        print("GET RECEP", name)
        for elem in self.recipes_list.keys():
            if self.recipes_list[elem].get(name):
                display = str(self.recipes_list[elem][name])
                print(display)

    def get_recipes_by_types(self, recipe_type):
        if recipe_type in self.recipes_list:
            for elem in self.recipes_list[recipe_type].keys():
                print("- ", elem)

    def add_recipe(self, recipe):
        if isinstance(recipe, Recipe):
            if "cookies" in self.recipes_list[recipe.recipe_type].keys():
                error = recipe.name + " already exist in books for "
                error += recipe.recipe_type + " meal"
                print(error)
            self.recipes_list[recipe.recipe_type][recipe.name] = recipe
        else:
            print("Not ok")
