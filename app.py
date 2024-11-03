# app.py
from flask import Flask
from models import db
from routes import api

app = Flask(__name__)

# Example database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Register the routes
app.register_blueprint(api)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates the database tables if they don't exist
    app.run(debug=True)
