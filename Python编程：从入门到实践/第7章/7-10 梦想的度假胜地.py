places = {}
while True:
    name = input("What is your name? ")
    if name == 'Q':
        break
    else:
        place = input("If you could visit one place in the world, where would you go? ")
        print()
        places[name] = place
print()
for name, place in places.items():
    print(name + " want to visit " + place + '.')