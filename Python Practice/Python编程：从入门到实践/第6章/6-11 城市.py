information_1 = {'country':"China", 'population':3000, 'fact':"C"}
information_2 = {'country':"USA", 'population':200, 'fact':"B"}
information_3 = {'country':"China", 'population':1000, 'fact':"A"}

cities = {'Beijing':information_1,
          'New York':information_2,
          'Tangshan':information_3
          }

for city in cities.keys():
    print(city.title() + ':')
    for key, value in cities[city].items():
        print('\t' + key + ' : ' + str(value))