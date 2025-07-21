import math


def is_perfect_square(x):
    s = int(math.isqrt(x))
    return s * s == x


def is_fib(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)


def generate_lucas(limit):
    lucas = [2, 1]
    while lucas[-1] < limit:
        lucas.append(lucas[-1] + lucas[-2])
    return set(lucas)


def is_lucas(n):
    return n in generate_lucas(n + 100)


def is_close_to_golden_ratio(a, b, threshold=0.01):
    if b == 0:
        return False
    ratio = a / b
    phi = (1 + math.sqrt(5)) / 2
    return abs(ratio - phi) < threshold


def menu():
    print("1. check if ratio of spike distances is close to the golden ratio")
    print("2. check if a number is a fib number")
    print("3. check if a number is a lucas number")
    print("4. exit")


def main():
    while True:
        menu()
        choice = input("enter your choice (1-4): ")

        if choice == "1":

            d1 = float(input("enter distance between first and second spike: "))
            d2 = float(input("enter distance between first and third spike: "))
            if is_close_to_golden_ratio(d2, d1):
                print("the ratio of distances is close to the golden ratio ")
            else:
                print("the ratio is not close to the golden ratio.")


        elif choice == "2":
            try:
                num = int(input("enter an integer: "))
                if is_fib(num):
                    print(f"{num} is a fib number.")
                else:
                    print(f"{num} is not a fib number.")
            except Valueerror:
                print("please enter a valid integer.")

        elif choice == "3":
            try:
                num = int(input("enter an integer: "))
                if is_lucas(num):
                    print(f"{num} is a lucas number.")
                else:
                    print(f"{num} is NOt a lucas number.")
            except Valueerror:
                print("please enter a valid integer.")

        elif choice == "4":
            print("exiting program.")
            break

        else:
            print("Invalid choice. please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
