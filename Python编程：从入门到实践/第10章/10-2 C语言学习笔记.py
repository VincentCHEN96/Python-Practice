with open('learning_python.txt', 'r') as file_object:
    for content in file_object:
        print(content.replace('Python', 'C'))