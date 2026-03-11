# config.py

import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "super_secret_key"

    DATABASE = os.path.join(BASE_DIR, "database/database.db")

    UPLOAD_FOLDER = "static/uploads"

    HEATMAP_FOLDER = "static/heatmaps"

    MODEL_PATH = "models/model.h5"

    # Email configuration
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    MAIL_USERNAME = "your_email@gmail.com"
    MAIL_PASSWORD = "your_app_password"

    ADMIN_EMAIL = "admin@gmail.com"