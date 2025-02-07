import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    sum_divisors = 1
    sqrt_n = math.isqrt(n)
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n):
    digits = str(n)
    length = len(digits)
    total = sum(int(digit)**length for digit in digits)
    return total == n

def get_digit_sum(n):
    return sum(int(digit) for digit in str(abs(n)))

def get_parity(n):
    return "even" if n % 2 == 0 else "odd"

def get_properties(n):
    properties = []
    if is_armstrong(n):
        properties.append("armstrong")
    if is_prime(n):
        properties.append("prime")
    if is_perfect(n):
        properties.append("perfect")
    properties.append(get_parity(n))
    return properties