from flask import Flask
import sqlite3


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'lmaolmaolmaolmao'
    DATABASE = "fridge.db"
    

    def initialize_db():
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS ingredients (name TEXT, quantity INTEGER)")
        conn.commit()
        conn.close()
    
    initialize_db()
        
    from .views import views
    from .auth import auth
    from .app import fridge
    
    app.register_blueprint(views, url_prefix ='/')
    app.register_blueprint(auth, url_prefix ='/')
    app.register_blueprint(fridge, url_prefix ='/')


    return app