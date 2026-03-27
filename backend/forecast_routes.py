from flask import Blueprint, jsonify
from backend.model import Forecast, db  # <-- changed

forecast_bp = Blueprint('forecast', __name__)

@forecast_bp.route('/all', methods=['GET'])
def get_forecasts():
    forecasts = Forecast.query.all()
    result = [
        {"product_name": f.product_name, "sales_quantity": f.sales_quantity}
        for f in forecasts
    ]
    return jsonify(result)
