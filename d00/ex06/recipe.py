class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

cookbook = {
}

cookbook['sandwich'] = {}
cookbook['sandwich']['ingredients'] = ['ham', 'bread', 'cheese', 'tomatoes']
cookbook['sandwich']['meal'] = 'lunch'
cookbook['sandwich']['prep_time'] = 10


cookbook['cake'] = {}
cookbook['cake']['ingredients'] = ['flour', 'sugar', 'eggs']
cookbook['cake']['meal'] = 'dessert'
cookbook['cake']['prep_time'] = 60

cookbook['salad'] = {}
cookbook['salad']['ingredients'] = ['avocado', 'arugula', 'tomatoes', 'spinach']
cookbook['salad']['meal'] = 'lunch'
cookbook['salad']['prep_time'] = 15


class Cookbook:
    def __init__(self):
        self.cookbook = cookbook
    def printRecipe(self,name):
        try:
            if name in self.cookbook:
                print("Recipe for ", name)
                print ("ingredients list", self.cookbook[name]['ingredients'])
                print("To be eaten for ", self.cookbook[name]['meal'])
                print("Takes ", self.cookbook[name]['prep_time'], "to be cooking.")
            else:
                raise ValueError("This is not ", name, " in the cookbook")
        except ValueError as err:
            print (err)

    def deleteRecipe(self, name):
        if name in self.cookbook:
            del self.cookbook[name]

    def addNewRecipe(self,name, ingredients, mealType, prep_time):
        try:
            if name in self.cookbook:
                raise KeyError("Recipe exist in cookbook")
            else:
                if isinstance(prep_time, int) and isinstance(ingredients, list) and isinstance( name, str) and isinstance(name, str):
                    self.cookbook[name] = {}
                    self.cookbook[name]['ingredients'] = ingredients
                    self.cookbook[name]['meal'] = mealType
                    self.cookbook[name]['prep_time'] = prep_time
                else:
                    raise ValueError("Verify your parameter\nUsage : addNewRecipe(name, ingredients, mealType, prep_time)\nname, mealType => str \ningredients => list \nprep_time => int")
        except (KeyError, ValueError) as err:
            print(err)

    def printAllRecipe(self):
        for recipe in self.cookbook:
            print (" * ", recipe)


def printUsage():
    print(bcolors.OKBLUE +"Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit" +  bcolors.ENDC)


def choice(nb):
    switcher = {
        1:'a',
        2:'b',
        3:'c',
        4:'d',
        5: "Cookbook is closed."
    }
    print(nb, switcher[nb])
    return switcher.get(nb, "Invalid number")

def main():
    nb = 0 
    livre = Cookbook()
    try:
        while  True:
            printUsage()
            nb = input(">>")
            if nb.isnumeric():
                choice = int(nb)
                if choice == 1:
                    recipeName = input("Please enter recipe name\n >> ")
                    ingredients = input("Please enter recipe ingredients\n >> ")
                    mealType = input("Please enter recipe meal type\n >> ")
                    prep_time = input("Please enter recipe preparation time\n >> ")
                    livre.addNewRecipe(recipeName, ingredients, mealType, prep_time)
                if choice == 2:
                    recipeNameToDelete = input("Please enter recipe name\n >> ")
                    if isinstance(recipeNameToDelete, str):
                        livre.deleteRecipe(recipeNameToDelete)
                if choice == 3:
                    recipeName = input("Please enter recipe name\n>> ")
                    if isinstance(recipeName, str):
                        livre.printRecipe(recipeName)
                if choice == 4:
                    livre.printAllRecipe()
                if choice == 5:
                    print("Cookbook is closed")
                    exit()
            else:
                print (bcolors.WARNING + "This option does not exist, please type the corresponding number." +bcolors.ENDC)
    except KeyboardInterrupt :
        exit()

if __name__ == "__main__":
    main()
