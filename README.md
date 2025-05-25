# Number Classification API 🔢

A RESTful API that analyzes numbers and returns their mathematical properties along with interesting fun facts.

## 🚀 Live API

**Base URL:** `https://flask-number-classification-api.onrender.com` (Replace with your actual deployment URL)

## 📋 Features

- ✅ Prime number detection
- ✅ Perfect number detection  
- ✅ Armstrong number detection
- ✅ Digit sum calculation
- ✅ Parity classification (odd/even)
- ✅ Fun mathematical facts from Numbers API
- ✅ CORS enabled
- ✅ Comprehensive error handling
- ✅ Fast response times (< 500ms)

## 🛠️ Technology Stack

- **Language:** Python 🐍
- **Framework:** Flask
- **Deployment:** Render 
- **External API:** Numbers API for fun facts

## 📖 API Documentation

### Endpoint

```
GET /api/classify-number?number={integer}
```

### Parameters

| Parameter | Type    | Required | Description                    |
|-----------|---------|----------|--------------------------------|
| number    | integer | Yes      | The number to analyze          |

### Response Format

#### Success Response (200 OK)

```json
{
  "number": 371,
  "is_prime": false,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 11,
  "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

#### Error Response (400 Bad Request)

```json
{
  "number": "alphabet",
  "error": true
}
```

### Properties Array Combinations

The `properties` field can contain the following combinations:

- `["armstrong", "odd"]` - Number is both Armstrong and odd
- `["armstrong", "even"]` - Number is Armstrong and even  
- `["odd"]` - Number is odd but not Armstrong
- `["even"]` - Number is even but not Armstrong

## 🧮 Mathematical Concepts

### Armstrong Numbers
An Armstrong number (also known as narcissistic number) is a number that equals the sum of its own digits each raised to the power of the number of digits.

**Examples:**
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
- 371 = 3³ + 7³ + 1³ = 27 + 343 + 1 = 371

### Prime Numbers
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.

### Perfect Numbers
A perfect number is a positive integer that is equal to the sum of its proper positive divisors.

**Example:** 6 = 1 + 2 + 3 (proper divisors of 6)

## 📝 Usage Examples

### Valid Requests

```bash
# Test Armstrong number
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=371"

# Test prime number
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=17"

# Test perfect number
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=28"

# Test regular number
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=42"
```

### Invalid Requests

```bash
# Non-numeric input
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=abc"

# Missing parameter
curl "https://flask-number-classification-api.onrender.com/api/classify-number"
```

## 🚀 Local Development

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/onomeakpobaro/flask_number_classification_api.git
   cd flask_number_classification_api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Test the API**
   ```bash
   curl "http://localhost:5000/api/classify-number?number=371"
   ```



### Render Deployment

1. Connect your GitHub repository to Render
2. Choose "Web Service"
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `gunicorn app:app`

## 🧪 Testing

### Manual Testing

```bash
# Test various number types
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=1"      # Neither prime nor perfect
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=2"      # Prime
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=6"      # Perfect
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=153"    # Armstrong
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=1634"   # Armstrong (4-digit)
```

### Error Testing

```bash
# Test error handling
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number=abc"    # Invalid input
curl "https://flask-number-classification-api.onrender.com/api/classify-number?number="       # Empty parameter
curl "https://flask-number-classification-api.onrender.com/api/classify-number"              # Missing parameter
```

## 📊 Performance

- **Response Time:** < 500ms (as required)
- **Uptime:** 99.9% (deployment dependent)
- **Rate Limiting:** None (consider adding for production)

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| PORT     | Server port | 5000    |
| DEBUG    | Debug mode  | False   |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request



## 🙏 Acknowledgments

- [Numbers API](http://numbersapi.com/) for providing interesting mathematical facts
- Flask community for the excellent web framework
- Mathematical concepts from various educational resources


---

**Made with ❤️ and Python** 🐍