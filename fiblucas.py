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


def classify_number(n):
    is_fib = is_fibonacci(n)
    lucas_set = generate_lucas(n + 100)  
    is_lucas = n in lucas_set

    if is_fib and is_lucas:
        return f"{n} is both a Fibonacci and a Lucas number."
    elif is_fib:
        return f"{n} is a Fibonacci number."
    elif is_lucas:
        return f"{n} is a Lucas number."
    else:
        return f"{n} is neither a Fibonacci nor a Lucas number."


if __name__ == "__main__":
    number = int(input("Enter an integer: "))
    result = classify_number(number)
    print(result)
