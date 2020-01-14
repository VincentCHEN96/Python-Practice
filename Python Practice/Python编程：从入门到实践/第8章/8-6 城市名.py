def city_country(name, country):
    cc = '"' + str(name).title() + ', ' + str(country).title() + '"'
    return cc


print(city_country("Santiago", "Chile"))
print(city_country("Beijing", "China"))
print(city_country("London", "England"))