import json


try:
    with open('favorite_number.json', 'r') as file_object:
        favorite_number = json.load(file_object)
        print("I know your favorite number! It's " + str(favorite_number) + '.')
except FileNotFoundError:
    with open('favorite_number.json', 'w') as file_object:
        favorite_number = input("Please input your favorite number: ")
        json.dump(favorite_number, file_object)