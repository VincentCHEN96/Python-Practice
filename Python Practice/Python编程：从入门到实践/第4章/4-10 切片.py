results = [result ** 3 for result in range(1, 11)]
for result in results :
	print(result)

print("The first three items in the list are:")
for result in results[:3]:
    print(result)

print("Three items from the middle of the list are:")
for result in results[2:5]:
    print(result)

print("The last three items in the list are:")
for result in results[-3:]:
    print(result)