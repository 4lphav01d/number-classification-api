import requests

def get_fun_fact(number):
    try:
        response = requests.get(
            f"http://numbersapi.com/{number}/math",
            params={'json': True},
            timeout=3
        )
        if response.status_code == 200:
            return response.json().get('text', "No fun fact available")
    except (requests.exceptions.RequestException, KeyError):
        pass
    return "No fun fact available"