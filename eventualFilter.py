def filterMenu():
    while(True):
        print("""What would you like the filter the recipes by?
              1. Meal Type
              2. Cooking Style
              3. Have I made this before?""")
        choice = input()
        if (int(choice) == 1):
            mealTypeFilterMenu()
            return
        elif (int(choice) == 2):
            cookingStyleFilterMenu()
            return
        elif (int(choice) == 3):
            haveMadeFilterMenu()
            return
        else:
            print("Please enter a valid option")

def mealTypeFilterMenu():
    while(True):
        print("""What meal type would you like?
              1. Breakfast
              2. Side
              3. Dinner
              4. Dessert
              5. Drink""")
        choice = input()
        if (int(choice) == 1):
            viewRecipeByFilter("mealType","Breakfast")
            return
        elif (int(choice) == 2):
            viewRecipeByFilter("mealType","Side")
            return
        elif (int(choice) == 3):
            viewRecipeByFilter("mealType","Dinner")
            return
        elif (int(choice) == 4):
            viewRecipeByFilter("mealType","Dessert")
            return
        elif (int(choice) == 5):
            viewRecipeByFilter("mealType","Drink")
            return
        else:
            print("Please enter a valid option")

def cookingStyleFilterMenu():
    while(True):
        print("""What cook style would you like?
              1. Stove Top
              2. Crock Pot
              3. Oven
              4. Table Top
              """)
        choice = input()
        if (int(choice) == 1):
            viewRecipeByFilter("cookType","Stove Top")
            return
        elif (int(choice) == 2):
            viewRecipeByFilter("cookType","Crock Pot")
            return
        elif (int(choice) == 3):
            viewRecipeByFilter("cookType","Oven")
            return
        elif (int(choice) == 4):
            viewRecipeByFilter("cookType","Table Top")
            return
        else:
            print("Please enter a valid option")    
            
def haveMadeFilterMenu():
    while(True):
        print("""Have you made this recipe before?
              1. Yes
              2. No""")
        choice = input()
        if (int(choice) == 1):
            viewRecipeByFilter("haveMade", "Yes")
            return
        elif (int(choice) == 2):
            viewRecipeByFilter("haveMade", "No")
            return
        else:
            print("Please enter a valid option")


def viewRecipeByFilter(column, item):
    c.execute("""SELECT name FROM recipe WHERE :column = :item """,{"column": column, "item": item})
    print(c.fetchall())
    recipeDetailsMenu()