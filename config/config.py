import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key_here')
