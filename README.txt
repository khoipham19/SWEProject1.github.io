# Fridge Inventory Application

## Overview
This Flask application serves as a digital inventory for tracking ingredients in a fridge. It allows users to add, remove, and view ingredients, as well as providing a dedicated recipes page.

## Features
- **Login Page:** A starting point for user authentication
- **Fridge Page:** Main page for managing the fridge inventory.
- **Recipes Page:** Dedicated page for viewing and managing recipes.
- **Ingredient Management:** Users can add or remove ingredients from the fridge inventory.
- **View Inventory:** A complete list view of all ingredients available in the fridge.

## How to Run
1. Ensure you have Python and Flask installed on your machine.
2. Navigate to the root directory of the project in your terminal or command prompt.
3. Run the application using: main.py (so python main.py) 
4. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Technologies Used
- Flask: A micro web framework written in Python.
- SQLite: A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.

## Directory Structure
- `app.py`: Main application file containing Flask routes.
- `functions.py`: Contains the core logic for database operations and ingredient management.
- `templates/`: Directory containing HTML templates for the application.
- `static/`: Directory containing static files like CSS and JavaScript.
- `fridge.db`: SQLite database file for storing ingredient data.

## Notes
- The application is currently in a development stage with a focus on backend functionality. Frontend design and user authentication are areas for future development.
- The SQLite database (`fridge.db`) is used for local storage and testing purposes.

