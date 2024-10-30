import sqlite3

connect = sqlite3.connect("recipe_party.db")

c = connect.cursor()

connect.commit()


class Recipe:
    def __init__(self, name, mealType, haveMade, cookType, ingredients, directions) -> None:
        self.name = name
        self.mealType = mealType
        self.haveMade = haveMade
        self.cookType = cookType
        self.ingredients = ingredients
        self.directions = directions

def newRecipe():
    name = getRecipeName()
    mealType = getMealType()
    haveMade = getHaveMade()
    cookStyle = getCookStyle()
    ingredients = getIngredients()
    directions = getDirections()

    recipe1 = Recipe(name, mealType, haveMade, cookStyle, ingredients, directions)
    
    createRecipeInDataBase(recipe1)
    #addIngredientsInDataBase(recipe1)
    #addDirectionsInDataBase(recipe1)

def createRecipeInDataBase(recipe: Recipe):
    c.execute("INSERT INTO recipe VALUES(:name, :mealType, :haveMade, :cookStyle)", {"name": recipe.name, "mealType": recipe.mealType, "haveMade": recipe.haveMade, "cookStyle": recipe.cookType})

def addIngredientsInDataBase(recipe: Recipe):
    for i in recipe.ingredients:
        c.execute("INSERT INTO ingredients VALUES(:name, :ingredient)", {"name": recipe.name, "ingredient": i})

def addDirectionsInDataBase(recipe: Recipe):
    for i in recipe.directions:
        c.execute("INSERT INTO directions VALUES(:name, :direction)", {"name": recipe.name, "direction": i})


def getMealType():
    while(True):
        print("""What meal type is this?
              1. Breakfast
              2. Side
              3. Dinner
              4. Dessert
              5. Drink""")
        choice = input()
        if (int(choice) == 1):
            return "Breakfast"
        elif (int(choice) == 2):
            return "Side"
        elif (int(choice) == 3):
            return "Dinner"
        elif (int(choice) == 4):
            return "Dessert"
        elif (int(choice) == 5):
            return "Drink"
        else:
            print("Please enter a valid option")

def getCookStyle():
    while(True):
        print("""What cook style is this?
              1. Stove Top
              2. Crock Pot
              3. Oven
              4. Table Top
              """)
        choice = input()
        if (int(choice) == 1):
            return "Stove Top"
        elif (int(choice) == 2):
            return "Crock Pot"
        elif (int(choice) == 3):
            return "Oven"
        elif (int(choice) == 4):
            return "Table Top"
        else:
            print("Please enter a valid option")

def getIngredients():
    ingredients = []
    while(True):
        ingredients.append(input("Enter ingredient and amount needed: "))
        print(f"""Add another ingredient?
              1. Yes
              2. No""")
        choice = input()
        if (int(choice) == 1):
            pass
        elif (int(choice) == 2):
            return ingredients
        else:
            print("Please enter a valid option")

def getDirections():
    directions = []
    while(True):
        directions.append(input("Add Direction: "))
        print(f"""Add another step?
              1. Yes
              2. No""")
        choice = input()
        if (int(choice) == 1):
            pass
        elif (int(choice) == 2):
            return directions
        else:
            print("Please enter a valid option")

def getRecipeName():
    name = input("Enter recipe name: ")
    while(True):
        print(f"""Is {name} correct?
              1. Yes
              2. No""")
        choice = input()
        if (int(choice) == 1):
            return name
        elif (int(choice) == 2):
            getRecipeName()
        else:
            print("Please enter a valid option")

def getHaveMade():
    while(True):
        print("""Have you made this recipe before?
              1. Yes
              2. No""")
        choice = input()
        if (int(choice) == 1):
            return "Yes"
        elif (int(choice) == 2):
            return "No"
        else:
            print("Please enter a valid option")


def viewRecipesMenu():
    print("""View Recipes Menu!
            Enter the number of what you would like to do!
            1. View All Recipes
            2. Search Recipe by Name
            3. Search Recipe by Tag
            4. Exit""")
    choice = input()
    if int(choice) == 1:
            viewAllRecipe()
    elif int(choice) == 2:
            name = input("Enter Recipe Name: ")
            viewRecipeByName(name)
    elif int(choice) == 3:
            #viewRecipeByFilter()
            print("ok")
    elif int(choice) == 4:
        return
    else:
        print("Type in a valid option please!")

def filterMenu():
    pass

def viewRecipeByFilter(column, item):
    c.execute("""SELECT name FROM recipe WHERE :column = :item """,{"column": column, "item": item})
    print(c.fetchall())

def viewAllRecipe():
    c.execute("""SELECT name FROM recipe""")
    print(c.fetchall())

def viewRecipeByName(name):
    c.execute("""SELECT name FROM recipe WHERE name = :name""",{"name": name})
    print(c.fetchall())

def deleteRecipe(name):
    c.execute("DELETE from recipes WHERE name = :name""",{"name": name})
    c.execute("DELETE from ingredients WHERE recipeName = :name""",{"name": name})
    c.execute("DELETE from directions WHERE recipeName = :name""",{"name": name})

def editRecipe():
    pass

def mainMenu():
    while (True):
        print("""Welcome to the Recipe Party!
            Enter the number of what you would like to do!
            1. Add Recipe
            2. Search Recipe
            3. Edit Recipe
            4. Delete Recipe
            5. Exit""")
        choice = input()
        if int(choice) == 1:
            newRecipe()
        elif int(choice) == 2:
            viewRecipesMenu()
        elif int(choice) == 3:
            editRecipe()
        elif int(choice) == 4:
            name = input("Enter Name of Recipe you want to Delete: ")
            deleteRecipe(name)
            print("Okay")
        elif int(choice) == 5:
            return
        else:
            print("Type in a valid option please!")

mainMenu()
connect.close()    