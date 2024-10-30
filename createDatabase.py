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
c.execute("""INSERT INTO ingredients VALUES('Pepper Lunch','1 cup Rice'), ('Pepper Lunch','1 tsp Soy Sauce'),
          ('Pepper Lunch','1 tsp Honey'), ('Pepper Lunch','1 tsp vinegar'), ('Pepper Lunch','1 tsp Garlic'), 
          ('Pepper Lunch','1/2 tsp Black Pepper'), ('Pepper Lunch','1 Cup Water'), ('Pepper Lunch','1 Onion Sliced'),
          ('Pepper Lunch','1/4 Cup Corn'), ('Pepper Lunch','150g Thinly Sliced Beef'), ('Pepper Lunch','1 tbsp Butter'),
          ('Pepper Lunch','1-2 Stalks Spring Onion'), ('Pepper Lunch','1/2 tsp sesame seeds')""")
c.execute("""INSERT INTO directions VALUES('Pepper Lunch','Rinse rice with water about 2-3 times, or until the water runs clear. Add rice to rice cooker pot.'),
          ('Pepper Lunch','Add light soy sauce, honey, vinegar, garlic, black pepper and dark soy sauce, if using. Pour in water. Stir to combine and level out the rice.'),
          ('Pepper Lunch','Layer on sliced onions, corn and the beef slices. Top with more freshly ground black pepper.'),
          ('Pepper Lunch','Place pot in rice cooker, and turn the rice cooker on to regular settings.'),
          ('Pepper Lunch','Once rice cooker is done cooking, open the lid. Add butter, spring onions and sesame seeds. Immediately stir to combine, allowing butter to melt into the rice.'),
          ('Pepper Lunch','Scoop Pepper Lunch onto plates and serve immediately!
Did you make this recipe?')""")
c.execute("INSERT INTO recipe VALUES('Strawberry Cream Cheese French Toast', 'Breakfast', 'Yes', 'Stove')")
c.execute("INSERT INTO recipe VALUES('Brown Butter-Maple Shortbread Bear Cookies', 'Dessert', 'No', 'Oven')")


          
c.execute("SELECT * FROM recipe")

print(c.fetchall())

connect.commit()
connect.close()
