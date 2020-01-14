with open('guest.txt', 'w') as file_object:
    name = input("Please input your name: ")
    file_object.write(name + '\n')