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
cookbook['sandwich']['ingredients'] = [
    'ham',
    'bread',
    'cheese',
    'tomatoes']
cookbook['sandwich']['meal'] = 'lunch'
cookbook['sandwich']['prep_time'] = 10


cookbook['cake'] = {}
cookbook['cake']['ingredients'] = [
    'flour',
    'sugar',
    'eggs']
cookbook['cake']['meal'] = 'dessert'
cookbook['cake']['prep_time'] = 60

cookbook['salad'] = {}
cookbook['salad']['ingredients'] = [
    'avocado',
    'arugula',
    'tomatoes',
    'spinach']
cookbook['salad']['meal'] = 'lunch'
cookbook['salad']['prep_time'] = 15


class Cookbook:
    def __init__(self):
        self.cookbook = cookbook

    def printRecipe(self, name):
        try:
            if name in self.cookbook:
                prep_time = self.cookbook[name]['prep_time']
                print("Recipe for ", name)
                print("Ingredients list", self.cookbook[name]['ingredients'])
                print("To be eaten for ", self.cookbook[name]['meal'])
                print("Takes ", prep_time, "to be cooking.")
            else:
                raise ValueError("There is not ", name, " in the cookbook")
        except ValueError as err:
            print(err)

    def deleteRecipe(self, name):
        if name in self.cookbook:
            del self.cookbook[name]

    def addNewRecipe(self, name, ingredients, meal, prep_time):
        try:
            if name in self.cookbook:
                raise KeyError("Recipe exist in cookbook")
            else:
                if prep_time.isnumeric()\
                    and isinstance(ingredients, list) \
                        and isinstance(name, str) and isinstance(meal, str):
                    self.cookbook[name] = {}
                    self.cookbook[name]['ingredients'] = ingredients
                    self.cookbook[name]['meal'] = meal
                    self.cookbook[name]['prep_time'] = int(prep_time)
                else:
                    check = "Verify your parameter\nUsage : addNewRecipe"
                    check += "(name, ingredients, mealType, prep_time)"
                    check += "\nname, mealType => str \ningredients => list \n"
                    check += "prep_time => int"
                    raise ValueError(check)
        except (KeyError, ValueError) as err:
            print(err)

    def printAllRecipe(self):
        for recipe in self.cookbook:
            print(" * ", recipe)


def printUsage():
    print(bcolors.OKBLUE, end="")
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit" + bcolors.ENDC)


def main():
    nb = 0
    livre = Cookbook()
    try:
        while True:
            printUsage()
            nb = input(">>")
            if nb.isnumeric():
                choice = int(nb)
                if choice == 1:
                    recipeName = input("Please enter recipe name\n >> ")
                    ingdients = input("Please enter recipe ingredients\n >> ")
                    mealType = input("Please enter recipe meal type\n >> ")
                    time = input("Please enter recipe preparation time\n >> ")
                    ingdtArray = ingdients.split()
                    livre.addNewRecipe(recipeName, ingdtArray, mealType, time)
                if choice == 2:
                    recipeToDelete = input("Please enter recipe name\n >> ")
                    if isinstance(recipeNameToDelete, str):
                        livre.deleteRecipe(recipeToDelete)
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
                e = "This option does not exist "
                e += "please type the corresponding number."
                print(bcolors.WARNING + "")
                print(e)
                print("" + bcolors.ENDC)
    except KeyboardInterrupt:
        exit()


if __name__ == "__main__":
    main()
