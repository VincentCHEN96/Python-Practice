with open('reason.txt', 'w') as file_object:
    while True:
        reason = input("Please input a reason about why you like Programming: ")
        if reason == 'Q' or reason == 'q':
            break
        file_object.write(reason + '\n')