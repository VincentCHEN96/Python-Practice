import json


with open('favorite_number.json', 'w') as file_object:
    favorite_number1 = input("Please input your favorite number: ")
    json.dump(favorite_number1, file_object)

with open('favorite_number.json', 'r') as file_object:
    favorite_number2 = json.load(file_object)
print("I know your favorite number! It's " + str(favorite_number2) + '.')