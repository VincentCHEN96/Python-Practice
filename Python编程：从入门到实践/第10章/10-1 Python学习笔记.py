with open('learning_python.txt', 'r') as file_object:
    content = file_object.read()
    print(content)

with open('learning_python.txt', 'r') as file_object:
    for content in file_object:
        print(content)

with open('learning_python.txt', 'r') as file_object:
    contents = file_object.readlines()

for content in contents:
    print(content)