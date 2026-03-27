from flask import Flask
from flask_cors import CORS
from backend.model import db
from backend.routes.forecast_routes import forecast_bp
from backend.routes.user_routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///retailiq.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    CORS(app)

    app.register_blueprint(forecast_bp, url_prefix='/forecast')
    app.register_blueprint(user_bp, url_prefix='/user')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
