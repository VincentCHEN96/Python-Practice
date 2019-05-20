with open('guest_book.txt', 'w') as file_object:
    while True:
        name = input("Please input your name: ")
        if name == 'Q' or name == 'q':
            break
        print("Hello, " + name + '\n')
        file_object.write(name + '\n')