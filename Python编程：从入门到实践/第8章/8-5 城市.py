def describe_city(name, country="China"):
    print(str(name).title() + " is in " + str(country).title() + ".")


describe_city('Beijing')
describe_city(name='Changsha')
describe_city(name='London', country='England')