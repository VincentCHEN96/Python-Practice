price = [0, 10, 15]
while True:
    age = int(input("Please input your age: "))
    if age < 3:
        print("Free.")
    elif age <= 12:
        print("Your price is " + str(price[1]))
    else:
        print("Your price is " + str(price[2]))