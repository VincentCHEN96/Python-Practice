class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("first name : " + self.first_name)
        print("last name : " + self.last_name)
        print("age : " + str(self.age))
        print("location : " + self.location)

    def greet_user(self):
        print("Hello, " + str(self.first_name).title() + str(self.last_name).title() + '.')


user = User('Vincent', 'CHEN', 23, 'Beijing')
user.describe_user()
user.greet_user()
user = User('Alina', 'XIE', 22, 'Changsha')
user.describe_user()
user.greet_user()
user = User('Crush', 'MENG', 23, 'Wuhan')
user.describe_user()
user.greet_user()
user = User('Josh', 'YU', 23, 'Luannan')
user.describe_user()
user.greet_user()