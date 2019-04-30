class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + str(self.restaurant_name).title() + '.')
        print("The restaurant's cuisine type is " + str(
            self.cuisine_type).title() + '.')

    def open_restaurant(self):
        print("The restaurant is opening.")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Chocolate', 'Milk']

    def show_flavors(self):
        print("The restaurant's ice cream flavors:")
        for flavor in self.flavors:
            print('\t' + flavor)


ice_cream_stand = IceCreamStand('KFC', 'Quick Food')
ice_cream_stand.show_flavors()