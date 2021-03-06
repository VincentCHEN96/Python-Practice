class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant name is " + str(self.restaurant_name).title() + '.')
        print("The restaurant's cuisine type is " + str(self.cuisine_type).title() + '.')
        print("The restaurant's served number is " + str(self.number_served) + '.')

    def open_restaurant(self):
        print("The restaurant is opening.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


restaurant = Restaurant('KFC', 'Quick Food')
print(restaurant.restaurant_name + ', ' + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(100)
restaurant.increment_number_served(10)
print(restaurant.number_served)