
import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.isqrt(n))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n <= 1:
        return False
    sum_divisors = 1
    sqrt_n = int(math.isqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

def is_armstrong(n):
    if n < 0:
        return False
    digits = str(n)
    length = len(digits)
    total = sum(int(digit)**length for digit in digits)
    return total == n

def get_digit_sum(n):
    return sum(int(d) for d in str(abs(n)))

def get_parity(n):
    return "even" if n % 2 == 0 else "odd"

def get_properties(n):
    properties = []
    n_abs = abs(n)

    if is_armstrong(n_abs):
        properties.append("armstrong")
    if is_prime(n_abs):
        properties.append("prime")
    if is_perfect(n_abs):
        properties.append("perfect")
    properties.append(get_parity(n))

    return sorted(properties)
