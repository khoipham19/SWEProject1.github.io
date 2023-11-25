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

if __name__ == "__main__":
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ingredients (name TEXT, quantity INTEGER)")
    conn.commit()
    app.run(debug=True)
