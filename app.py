from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = "fridge.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

@app.route('/')
def login():
    return render_template('login.html')

# Add a new route to serve the frontend:
@app.route('/fridge')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

# Remove the ingredient if less than 0
@app.route('/remove', methods = ['POST'])
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


@app.route('/add', methods=['POST'])
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

@app.route('/view', methods=['GET'])
def view_fridge():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ingredients")
    items = cursor.fetchall()
    return jsonify(items)

if __name__ == "__main__":
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ingredients (name TEXT, quantity INTEGER)")
    conn.commit()
    app.run(debug=True)
