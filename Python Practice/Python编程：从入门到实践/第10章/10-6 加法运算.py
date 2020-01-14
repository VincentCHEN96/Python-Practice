number1 = input("Please input a number: ")
number2 = input("Please input another number: ")

try:
    result = int(number1) + int(number2)
    print(result)
except ValueError:
    print("Your input may not be a number.")