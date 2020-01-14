try:
    with open('cats.txt', 'r') as file_object:
        content = file_object.read()
        print(content)

    with open('dogs0.txt', 'r') as file_object:
        content = file_object.read()
        print(content)
except FileNotFoundError:
    pass