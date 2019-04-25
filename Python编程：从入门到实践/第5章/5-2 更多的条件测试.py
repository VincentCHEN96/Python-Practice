string_1 = "This is a test string."
string_2 = "This is a signification string."
print(string_1 != string_2)
print(string_1 == string_2)

string = 'Hello'
print(string.lower() == 'hello')
print(string.lower() == 'Hello')

data_1 = 1
data_2 = 2
print(data_1 == data_2)
print(data_1 != data_2)
print(data_1 > data_2)
print(data_1 < data_2)
print(data_1 >= data_2)
print(data_1 <= data_2)

data = 9
print(data > 0 and data < 10)
print(data > 10 and data < 100)
print(data > 0 or data < 10)
print(data > 10 or data < 0)

list = [number for number in range(1, 6)]
print(1 in list)
print(0 in list)
print(0 not in list)
print(1 not in list)