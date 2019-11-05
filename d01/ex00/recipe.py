class Recipe:
    def __init__(self, name, cooklvl, cookTime, ingdts, descript, recipe_type):
        self.name = name
        self.cooking_level = cooklvl
        self.cooking_time = cookTime
        self.ingredients = ingdts
        self.description = descript
        self.recipe_type = recipe_type
        self.valueIsOK = True
        self.checkValue()

    def checkValue(self):
        self.checkString(self.name, "name")
        self.checkRecipeType()
        self.checkCookingLevel()
        self.checkCookingTime()
        self.checkIngrediensList()
        self.checkString(self.description, "descr")
        if not self.valueIsOK:
            exit()

    def checkString(self, value, attribute):
        if not isinstance(value, str) or (not value and attribute != "descr"):
            self.valueIsOK = False
            print(value, " for ", attribute, "is not valid")

    def checkRecipeType(self):
        recipe_type = ["lunch", "starter", "dessert"]
        if not (self.recipe_type in recipe_type):
            self.valueIsOK = False
            recipeStr = ", ".join(recipe_type)
            error = ""
            error += self.recipe_type
            error += " do not belong to available list"
            error += "\nPlease choose among this following type: "
            error += recipeStr
            print(error)

    def checkCookingLevel(self):
        if isinstance(self.cooking_level, int):
            if self.cooking_level in range(1, 6):
                return
        self.valueIsOK = False
        error = "Cooking Level " + str(self.cooking_level) + " is not valid"
        error += "Please enter a number between 1 and 5"
        print(error)

    def checkCookingTime(self):
        if isinstance(self.cooking_time, int):
            if self.cooking_time > 0:
                return
        self.valueIsOK = False
        error = "Cooking Time " + str(self.cooking_time) + " is not valid"
        error += "Please enter a positiv number "
        print(error)

    def checkIngrediensList(self):
        if isinstance(self.ingredients, list):
            for elem in self.ingredients:
                self.checkString(elem, "ingredients")
        else:
            self.valueIsOK = False
            print("Ingredients should be a list")

    def __str__(self):
        display = ""
        display += "Recipe for " + self.name
        display += "\nIngredients list \n - " + "\n - ".join(self.ingredients)
        display += "\nTo be eaten for " + str(self.recipe_type)
        display += "\nTakes " + str(self.cooking_time) + " minutes of cooking"
        return display