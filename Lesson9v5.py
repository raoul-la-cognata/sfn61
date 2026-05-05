num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

try:
    num1 = int(num1)
    num2 = int(num2)
except ZeroDivisionError as error:
    pass
except Exception as error:
    print("There is a problem with the numbers")
    print(error)

print("The script continued")

