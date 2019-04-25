while True:
    ingredient = input("Please input a ingredient of your pizza: ")
    if ingredient == 'quit':
        break
    else:
        print("We will add " + ingredient.upper() + " into your pizza.")