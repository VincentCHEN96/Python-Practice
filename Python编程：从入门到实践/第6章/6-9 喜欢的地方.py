favorite_place_1 = ['Xian', 'Chengdu', 'Beijing']
favorite_place_2 = ['Beijing', 'Shijiazhuang']
favorite_place_3 = ['Beijing', 'Tianjin', 'Wuhan']
favorite_places = {'vincent':favorite_place_1,
                   'josh':favorite_place_2,
                   'crush':favorite_place_3
                   }
for name, favorite_place in favorite_places.items():
    print(name.title() + "'s favorite place is:")
    for place in favorite_place:
        print('\t' + place.title())