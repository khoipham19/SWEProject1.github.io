import sqlite3
from flask import jsonify

DATABASE = "fridge.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def add_ingredient_function(data):

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

def remove_ingredient_function(data):
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
