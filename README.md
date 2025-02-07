

# Number Classifier API

A RESTful API built with Flask that accepts an integer and returns interesting mathematical properties about it—including whether it’s prime, perfect, an Armstrong number (if applicable), its parity, digit sum, and a fun math fact retrieved from NumbersAPI.

## Overview

The Number Classifier API exposes a single GET endpoint:

```
/api/classify-number?number=371
```

When provided a valid integer as a query parameter, the API returns a JSON response with the following structure:
- **number**: the integer provided
- **is_prime**: boolean indicating if the number is prime
- **is_perfect**: boolean indicating if the number is a perfect number
- **properties**: an array of string properties (e.g. `"armstrong"`, `"odd"`, or `"even"`)
- **digit_sum**: sum of the digits of the number
- **fun_fact**: a fun fact about the number (fetched from NumbersAPI)

For invalid input (e.g., non-numeric values), the API returns a 400 error along with an error message.

## Features

- **Input Validation:** Accepts only valid integers (handles negatives as well).
- **Mathematical Computations:** Checks if the number is prime, perfect, and (optionally) an Armstrong number; calculates digit sum and parity.
- **External API Integration:** Retrieves a fun fact from [NumbersAPI](http://numbersapi.com) using HTTP GET.
- **CORS Enabled:** Cross-Origin Resource Sharing is enabled via Flask-CORS for public accessibility.
- **Deployment Ready:** Designed to run on a VPS using Gunicorn (or another WSGI server) behind a reverse proxy like Nginx.

## Tech Stack

- **Python 3**
- **Flask** – for the web framework
- **Flask-CORS** – to enable cross-origin resource sharing
- **Requests** – for making HTTP requests to external APIs
- **Gunicorn** – recommended production WSGI server

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/number-classifier-api.git
   cd number-classifier-api
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
number-classifier-api/
├── app.py
├── http_client.py
├── number_service.py
├── requirements.txt
└── README.md
```

- **app.py:** Main Flask application with the `/api/classify-number` endpoint.
- **http_client.py:** Module for fetching the fun fact from NumbersAPI.
- **number_service.py:** Module for mathematical computations (prime, perfect, Armstrong, etc.).
- **requirements.txt:** Lists the dependencies.
- **README.md:** Project documentation.

## Usage

### Running Locally

To run the development server (do not use for production):

```bash
python app.py
```

This will start the Flask development server (with debug mode enabled) and you will see output similar to:

```
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://<your-local-ip>:5000
Press CTRL+C to quit
```

You can now test the endpoint in your browser or via curl:

```bash
curl "http://127.0.0.1:5000/api/classify-number?number=371"
```

### Expected JSON Response

For a valid request, you should receive a response similar to:

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

For invalid input (e.g., non-numeric):

```json
{
  "number": "alphabet",
  "error": true
}
```

## Deployment on a VPS

For production, it’s recommended to run your API using Gunicorn and to place Nginx as a reverse proxy. 

Here’s a quick outline:

1. **Clone your repo and install dependencies** as described in the Installation section on your VPS.
2. **Run Gunicorn:**
   ```bash
   gunicorn --bind 0.0.0.0:8000 app:app
   ```


## Contributing

Contributions are welcome! Feel free to fork the repository and open pull requests. 
