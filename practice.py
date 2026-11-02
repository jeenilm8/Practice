# Basic Python practice

def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


def factorial(number):
    if number < 0:
        raise ValueError("Number must be non-negative")

    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


if __name__ == "__main__":
    print("Addition:", add(10, 20))
    print("Is 8 even?", is_even(8))
    print("Factorial of 5:", factorial(5))
