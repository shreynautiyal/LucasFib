import math


def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x


def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def generate_lucas(limit):
    lucas = [2, 1]
    while lucas[-1] < limit:
        lucas.append(lucas[-1] + lucas[-2])
    return set(lucas)


def is_close_to_golden_ratio(n, threshold=0.01):
    phi = (1 + math.sqrt(5)) / 2
    for b in range(1, 100):
        ratio = n / b
        if abs(ratio - phi) < threshold:
            return True
    return False


def classify_number(n):
    is_fib = is_fibonacci(n)
    lucas_set = generate_lucas(n + 100)
    is_lucas = n in lucas_set
    is_phi_related = is_close_to_golden_ratio(n)

    if is_fib and is_lucas:
        return f"{n} is both a Fibonacci and a Lucas number."
    elif is_fib:
        return f"{n} is a Fibonacci number."
    elif is_lucas:
        return f"{n} is a Lucas number."
    elif is_phi_related:
        return f"{n} is not a Fibonacci or Lucas number, but is close to the golden ratio."
    else:
        return f"{n} is neither a Fibonacci number, a Lucas number, nor close to the golden ratio."


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    result = classify_number(number)
    print(result)
