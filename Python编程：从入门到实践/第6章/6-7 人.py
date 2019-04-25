vincent = {'first_name':"Weizheng",
           'last_name':"CHEN",
           'age':23,
           'city':"Beijing"
           }
alina = {'first_name':"Yi",
         'last_name':"XIE",
         'age':22,
         'city':"Changsha"
         }
crush = {'first_name':"Weiye",
         'last_name':"MENG",
         'age':23,
         'city':"Wuhan"
         }

people = [vincent, alina, crush]

for name in people:
    for key, value in name.items():
        print(key + ' : ' + str(value))