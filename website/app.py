from flask import Flask, request, jsonify, render_template, Blueprint
import sqlite3
fridge = Blueprint('fridge', __name__)
DATABASE = "fridge.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# Login page
@fridge.route('/')
def login():
    return render_template('login.html')

# Main page; function page; fridge page
@fridge.route('/fridge')
def index():
    return render_template('index.html')

# Recipes page
@fridge.route('/recipes')
def recipes():
    return render_template('recipes.html')

# Remove the ingredient
@fridge.route('/remove', methods = ['POST'])
def remove_ingredient():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM ingredients WHERE name=?", (data['name'],))
    result = cursor.fetchone()

    if result:
        new_quantity = result[0] - int(data['quantity'])
        if new_quantity <= 0:
            cursor.execute("DELETE FROM ingredients WHERE name=?", (data['name'],))
        else:
            cursor.execute("UPDATE ingredients SET quantity=? WHERE name=?", (new_quantity, data['name'],))
    else:
        return jsonify({"message": "Ingredient not found!"})
    
    conn.commit()
    return jsonify({"message": "Ingredient removed!"})

# Add the ingredient
@fridge.route('/add', methods=['POST'])
def add_ingredient():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM ingredients WHERE name=?", (data['name'],))
    result = cursor.fetchone()

    if result:
        new_quantity = result[0] + int(data['quantity'])
        cursor.execute("UPDATE ingredients SET quantity=? WHERE name=?", (new_quantity, data['name']))

    
    else:
        cursor.execute("INSERT INTO ingredients (name, quantity) VALUES (?, ?)", (data['name'], data['quantity'],))

    conn.commit()
    return jsonify({"message": "Ingredient added!"})

# View the fridge in list
@fridge.route('/view', methods=['GET'])
def view_fridge():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredients")
    items = cursor.fetchall()
    return jsonify(items)



# Add recipe and ingredients to the database
@fridge.route('/add_recipe', methods=['POST'])
def add_recipe():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO recipes (name, ingredients) VALUES (?, ?)", (data['name'].lower(), data['ingredients'].lower(),))
    conn.commit()
    return jsonify({"message": "Recipe added!"})

# View avaiable recipes based on available ingredients
@fridge.route('/view_recipes', methods=['GET'])
def view_recipes():
    # Recipes with their required ingredients
    recipes_dict = {
        "English Breakfast": ["Egg", "Bacon"],
        # "Recipe2": ["ingredient3", "ingredient4"],
        # Add more recipes as needed
    }

    # Fetch ingredients from the database
    conn = get_db()
    cursor = conn.cursor()


    # fetch all ingredients from the database
    cursor.execute("SELECT * FROM ingredients")
    avaiable_ingredients = {item[0] for item in cursor.fetchall()}
    print(avaiable_ingredients)

    # fetch all recipes from the database
    cursor.execute("SELECT * FROM recipes")
    recipes = cursor.fetchall()
    print(recipes)
    
    cursor.execute("SELECT name FROM ingredients")
    available_items = [item[0] for item in cursor.fetchall()]


    possible_recipes = []
    for recipe, required_ingredients in recipes_dict.items():
        if all(ingredient in available_items for ingredient in required_ingredients):
            possible_recipes.append(recipe)

    return jsonify(possible_recipes)

