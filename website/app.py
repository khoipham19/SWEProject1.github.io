from flask import Flask, request, jsonify, render_template
from functions import get_db, add_ingredient_function, remove_ingredient_function, view_fridge_function
import sqlite3

app = Flask(__name__)
DATABASE = "fridge.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

# Login page
@app.route('/')
def login():
    return render_template('login.html')

# Main page; function page; fridge page
@app.route('/fridge')
def index():
    return render_template('index.html')

# Recipes page
@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

# Remove the ingredient
@app.route('/remove', methods = ['POST'])
def remove_ingredient():
    data = request.json
    return remove_ingredient_function(data)

# Add the ingredient
@app.route('/add', methods=['POST'])
def add_ingredient():
    data = request.json
    return add_ingredient_function(data)

# View the fridge in list
@app.route('/view', methods=['GET'])
def view_fridge():
    return view_fridge_function()

# View avaiable recipes based on available ingredients
@app.route('/view_recipes', methods=['GET'])
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
    cursor.execute("SELECT name FROM ingredients")
    available_items = [item[0] for item in cursor.fetchall()]

    # Find which recipes can be made with available ingredients
    possible_recipes = []
    for recipe, required_ingredients in recipes_dict.items():
        if all(ingredient in available_items for ingredient in required_ingredients):
            possible_recipes.append(recipe)

    return jsonify(possible_recipes)

if __name__ == "__main__":
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ingredients (name TEXT, quantity INTEGER)")
    conn.commit()
    app.run(debug=True)
