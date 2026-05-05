num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    division = num1 / num2
    print(f"{num1}/{num2} = {division}")
except (NameError, ZeroDivisionError, ValueError):
    print("Error: Check that numbers are integers and second number is not zero")