from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import number_service
import http_client

app = Flask(__name__)
CORS(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')

    if not number_str:
        return jsonify({"number": "undefined", "error": True}), 400

    try:
        # Allow integers and floats that are effectively integers (e.g., 123.0)
        number = float(number_str)
        if not number.is_integer():
            return jsonify({"number": number_str, "error": True}), 400
        number = int(number)
    except ValueError:
        return jsonify({"number": number_str, "error": True}), 400
    
    properties = number_service.get_properties(number)
    digit_sum = number_service.get_digit_sum(number)
    fun_fact = http_client.get_fun_fact(number)
    
    return jsonify({
        "number": number,
        "is_prime": number_service.is_prime(number),
        "is_perfect": number_service.is_perfect(number),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact
    })

if __name__ == '__main__':
    app.run(debug=True)