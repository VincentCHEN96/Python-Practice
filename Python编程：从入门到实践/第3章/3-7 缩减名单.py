guests = ['Jobs', 'Jack Ma', 'Pony Ma']
for guest in guests:
    invitation = "Hello, " + guest + ". I would like to invite you to join my party."
    print(invitation)

print("But unfortunately, " + guests[0] + " can not come.")

guests[0] = 'Vincent'
for guest in guests:
    invitation = "Hello, " + guest + ". I would like to invite you to join my party."
    print(invitation)

print("Now I have found a bigger table.")

guests.insert(0, 'Aline')
guests.insert(2, 'Crush')
guests.append('Josh')
for guest in guests:
    invitation = "Hello, " + guest + ". I would like to invite you to join my party."
    print(invitation)

print("Unfortunately, I just can invite two gays tonight.")

while len(guests) > 2:
    pop_guest = guests.pop()
    apology = "Sorry, " + pop_guest + "."
    print(apology)
for guest in guests:
    message = guest + ", you are still in my inviting list."
    print(message)

for i in range(0, len(guests)):
    del guests[0]
print(guests)