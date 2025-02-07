
import requests

def get_fun_fact(number):
    try:
        response = requests.get(
            f"http://numbersapi.com/{number}/math",
            params={'json': True},
            timeout=3
        )
        if response.status_code == 200:
            return response.json().get('text', f"{number} is an interesting number!")
    except (requests.exceptions.RequestException, KeyError):
        pass
    return f"{number} is a fascinating number with unique properties."
