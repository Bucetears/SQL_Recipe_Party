import sqlite3

connect = sqlite3.connect("recipe_party.db")

c = connect.cursor()

c.execute("""CREATE TABLE recipe (
          name text,
          mealType text,
          haveMade text,
          cookType text)
          """)
c.execute("""CREATE TABLE ingredients (
          recipeName text,
          ingredient text
          )""")

c.execute("""CREATE TABLE directions (
          recipeName text,
          direction text
          )""")

c.execute("INSERT INTO recipe VALUES('Pepper Lunch', 'Dinner', 'Yes', 'Crock Pot')")
c.execute("INSERT INTO recipe VALUES('Strawberry Cream Cheese French Toast', 'Breakfast', 'Yes', 'Stove')")
c.execute("INSERT INTO recipe VALUES('Brown Butter-Maple Shortbread Bear Cookies', 'Dessert', 'No', 'Oven')")


          
c.execute("SELECT * FROM recipe")

print(c.fetchall())

connect.commit()
connect.close()
