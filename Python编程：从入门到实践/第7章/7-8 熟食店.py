sandwich_orders = ['apple sandwich', 'banana sandwich', 'tuna sandwich']
finished_sandwich = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich +".")
    finished_sandwich.append(sandwich)
print("All sandwich bellow are finished:")
for sandwich in finished_sandwich:
    print('\t' + sandwich)