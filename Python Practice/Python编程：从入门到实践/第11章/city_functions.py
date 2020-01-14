def city_country(city, country, population=''):
    if population:
        description = str(city) + ', ' + str(country) + ' - population ' + str(population)
    else:
        description = str(city) + ', ' + str(country)
    return description