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
    
    if not number_str or not number_str.lstrip('-').isdigit():
        return jsonify({
            "number": number_str if number_str else "undefined",
            "error": True
        }), 400
    
    number = int(number_str)
    
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