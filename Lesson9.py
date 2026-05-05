num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = int(num1)
except ValueError:
    print("Exiting: The first number is not a whole number.")
    exit()

try:
    num2 = int(num2)
except ValueError:
    print("Exiting: The second number is not a whole number.")
    exit()

try:
    division = num1 / num2
except ZeroDivisionError:
    print("Exiting: The second number cannot be zero.")

try:
    print(f"{num1}/{num2} = {division}")
except NameError:
    print("There was an error in printing the result")