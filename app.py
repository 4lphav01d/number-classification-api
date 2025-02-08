from flask import Flask, jsonify, request
from flask_cors import CORS
import number_service
import http_client
import math

app = Flask(__name__)
CORS(app)

# Middleware to set Content-Type header to application/json
@app.after_request
def add_json_header(response):
    if response.content_type == 'application/json':
        response.headers['Content-Type'] = 'application/json'
    return response

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number', '').strip()

    # Validate input and return JSON response with error message if invalid
    if not number_str:
        return jsonify({"error": "Number is required"}), 400

    try:
        num = float(number_str)
        if not num.is_integer() or math.isinf(num):
            raise ValueError
        number = int(num)
    except (ValueError, OverflowError):
        return jsonify({
            "error": "Invalid number format",
            #"number": number_str
            "number": "alphabet"

        }), 400

    # Calculate properties and return JSON response
    try:
        properties = number_service.get_properties(number)
        digit_sum = number_service.get_digit_sum(number)
        fun_fact = http_client.get_fun_fact(abs(number))  # Use absolute value for fact lookup

        return jsonify({
            "number": number,
            "is_prime": number_service.is_prime(abs(number)),
            "is_perfect": number_service.is_perfect(abs(number)),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({
            "error": "Internal server error",
            "number": number_str
        }), 500

# Error handler for 404 errors, returns JSON response
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found",
        "message": "The requested URL was not found on the server"
    }), 404

# Error handler for 500 errors, returns JSON response
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal server error",
        "message": "An unexpected error occurred"
    }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
