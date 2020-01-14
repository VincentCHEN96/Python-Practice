the_shy = {'type':"tiger", 'owner':"IG"}
ning = {'type':"dog", 'owner':"IG"}
rookie = {'type':"lion", 'owner':"IG"}
jkl = {'type':"fish", 'owner':"IG"}
bao_lan = {'type':"cat", 'owner':"IG"}

pets = [the_shy, ning, rookie, jkl, bao_lan]

for pet in pets:
    for key, value in pet.items():
        print(key + ' : ' + value)
    print()