num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
    division = num1 / num2
    print(f"{num1}/{num2} = {division}")
except NameError:
    print("There is a problem with the second.")
except ZeroDivisionError:
    print("The second number cannot be zero.")
except ValueError:
    print("Error: Check that the numbers are integers")