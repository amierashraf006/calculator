def multiply(a, b):
    return a * b

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = multiply(num1, num2)
    print(f"The product of {num1} and {num2} is {result}.")