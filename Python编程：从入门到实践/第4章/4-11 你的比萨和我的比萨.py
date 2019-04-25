pizzas = ['chick pizza', 'beef pizza', 'poke pizza']

for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    message = "I like " + pizza + '.'
    print(message)

print("I really like pizza!")

friend_pizzas = pizzas[:]
pizzas.append('banana pizza')
friend_pizzas.append('apple pizza')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)