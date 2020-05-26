cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
        },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomaotes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def exists(name):
    for x in cookbook:
        if x == name:
            return (True)
    return (False)


def print_recipe(name):
    if (exists(name)):
        print("\nRecipe for " + name + ":")
        print("Ingredients list: " + str(cookbook[name]["ingredients"]))
        print("To be eaten for " + str(cookbook[name]["meal"]))
        finph = " minutes of cooking\n"
        print("Takes " + str(cookbook[name]['prep_time']) + finph)
    else:
        print("No recipe under the name of " + name)


def delete_recipe(name):
    if (exists(name)):
        cookbook.pop(name)
        print(name + "recipe succesfully deleted !")
    else:
        print("no " + name + " recipe in the cookbook")


def print_names():
    for x in cookbook:
        print(x)


def add_recipe(name, meal, prep, ing):
    d = {name: {'ingredients': ing, 'meal': meal, 'prep_time': prep}}
    cookbook.update(d)


def get_list(phrase):
    phrase = phrase.replace(' ', '')
    phrase = phrase.split(',')
    print(phrase)
    return(phrase)


def menu():
    while 1:
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        try:
            choice = int(input())
        except:
            dernph = "please type the corresponding number."
            print("This option does not exist, " + dernph)
            print("To exit, enter 5.")
        if choice == 1:
            print("Please provide recipe name")
            name = input()
            print("Please provide ingredients seperated by commas")
            ing = input()
            ing = get_list(ing)
            print("Please provide prep time needed")
            prep = int(input())
            print("Please specify which type of meal this recipe belong to")
            meal = input()
            add_recipe(name, meal, prep, ing)
        elif choice == 2:
            print("Which recipe would you like to delete ?")
            name = input()
            delete_recipe(name)
        elif choice == 3:
            print("Which recipe would you like to print ?")
            name = input()
            print_recipe(name)
        elif choice == 4:
            print_names()
        elif choice == 5:
            print("\n\nCookBook closed")
            exit()
        else:
            dernph = "please type the corresponding number."
            print("This option does not exist, " + dernph)
            print("To exit, enter 5.")



menu()
