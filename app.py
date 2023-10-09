from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
DATABASE = "fridge.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn


# Add a new route to serve the frontend:
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove', methods = ['POST'])
def remove_ingredient():
    data = request.json
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("SELECT quantity FROM ingredients WHERE name=?", (data['name'],))
    result = cursor.fetchone()

    if result:
        new_quantity = result[0] - int(data['quantity'])
        cursor.execute("UPDATE ingredients SET quantity=? WHERE name=?", (new_quantity, data['name'],))
    else:
        cursor.execute("DELETE FROM ingredients (name, quantity) VALUES (?, ?)", (data['name'], data['quantity'],))
    
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

# @app.route('/remove', methods=['POST'])
# def remove_ingredient():
#     data = request.json
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM ingredients WHERE name=?", (data['name'],))
#     conn.commit()
#     return jsonify({"message": "Ingredient removed!"})

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
