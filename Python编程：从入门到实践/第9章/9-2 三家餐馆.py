class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is " + str(self.restaurant_name).title() + '.')
        print("The restaurant's cuisine type is " + str(self.cuisine_type).title() + '.')

    def open_restaurant(self):
        print("The restaurant is opening.")


restaurant = Restaurant('KFC', 'Quick Food')
restaurant.describe_restaurant()
restaurant = Restaurant('McDownloads', 'Quick Food')
restaurant.describe_restaurant()
restaurant = Restaurant('Pizza Huts', 'Quick Food')
restaurant.describe_restaurant()