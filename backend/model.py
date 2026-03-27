from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Forecast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    sales_quantity = db.Column(db.Integer, nullable=False)
    forecast_date = db.Column(db.Date, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)