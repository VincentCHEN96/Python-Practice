def add_ingredients(*ingredients):
    print("Your ingredients list:")
    for ingredient in ingredients:
        print('\t' + str(ingredient))


add_ingredients('Apple', 'Banana')
add_ingredients('Pear')
add_ingredients('Beef', 'chick', 'poke')