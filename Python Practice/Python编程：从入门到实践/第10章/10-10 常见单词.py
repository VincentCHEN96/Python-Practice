with open('gutenberg.txt', 'r') as file_object:
    content = file_object.read()
    print(content.count('the'))