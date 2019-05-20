while True:
    number1 = input("Please input a number: ")
    if number1 == 'Q' or number1 == 'q':
        break
    number2 = input("Please input another number: ")
    if number2 == 'Q' or number2 == 'q':
        break
    try:
        result = int(number1) + int(number2)
        print(result)
    except ValueError:
        print("Your input may not be a number.")