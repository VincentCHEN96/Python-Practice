sandwich_orders = ['apple sandwich', 'pastrami sandwich', 'banana sandwich', 'pastrami sandwich', 'tuna sandwich', 'pastrami sandwich']
finished_sandwich = []
print("Pastrami Sandwich has sold out.")
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich +".")
    finished_sandwich.append(sandwich)
print("All sandwich bellow are finished:")
for sandwich in finished_sandwich:
    print('\t' + sandwich)