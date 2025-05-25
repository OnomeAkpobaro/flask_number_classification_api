from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import math

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is perfect (sum of proper divisors equals the number)"""
    if n <= 1:
        return False
    
    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid counting the square root twice
                divisor_sum += n // i
    
    return divisor_sum == n

def is_armstrong(n):
    """Check if a number is an Armstrong number"""
    if n < 0:
        return False
    
    digits = str(abs(n))
    num_digits = len(digits)
    digit_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return digit_sum == abs(n)

def calculate_digit_sum(n):
    """Calculate the sum of digits"""
    return sum(int(digit) for digit in str(abs(n)))

def get_fun_fact(number):
    """Get fun fact from numbers API"""
    try:
        response = requests.get(f"http://numbersapi.com/{number}/math", timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return f"{number} is a number with its own unique mathematical properties."
    except:
        return f"{number} is a number with its own unique mathematical properties."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """Main API endpoint to classify a number"""
    try:
        # Get the number parameter
        number_param = request.args.get('number')
        
        if number_param is None:
            return jsonify({
                "error": True,
                "message": "Missing required parameter 'number'"
            }), 400
        
        # Validate that it's a valid integer
        try:
            number = int(number_param)
        except ValueError:
            return jsonify({
                "number": number_param,
                "error": True
            }), 400
        
        # Calculate mathematical properties
        prime_check = is_prime(number)
        perfect_check = is_perfect(number)
        armstrong_check = is_armstrong(number)
        digit_sum = calculate_digit_sum(number)
        
        # Determine properties array based on requirements
        properties = []
        if armstrong_check:
            properties.append("armstrong")
        
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
        
        # Get fun fact
        fun_fact = get_fun_fact(abs(number))
        
        # Return the response
        return jsonify({
            "number": number,
            "is_prime": prime_check,
            "is_perfect": perfect_check,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }), 200
        
    except Exception as e:
        return jsonify({
            "error": True,
            "message": "Internal server error"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"}), 200

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        "message": "Number Classification API",
        "endpoint": "/api/classify-number?number=<integer>",
        "example": "/api/classify-number?number=371",
        "documentation": "https://github.com/onomeakpobaro/flask_number_classification_api"
    }), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)