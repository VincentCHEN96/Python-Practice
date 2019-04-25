favorite_number_1 = [6, 7, 8, 9]
favorite_number_2 = [8, 9]
favorite_number_3 = [1, 2, 6, 7]
favorite_number_4 = [2, 3, 6, 8]
favorite_number_5 = [0, 1, 2, 3, 4, 5]
favorite_numbers = {'Josh':favorite_number_1,
                    'Crush':favorite_number_2,
                    'Alina':favorite_number_3,
                    'James':favorite_number_4,
                    'John':favorite_number_5
                    }
for name, numbers in favorite_numbers.items():
    print(name.title() + "'s favorite number is:")
    for number in numbers:
        print('\t' + str(number))