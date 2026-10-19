def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    try:
        result = divide(num1, num2)
        print(f"The result of dividing {num1} by {num2} is {result}.")
    except ValueError as e:
        print(e)