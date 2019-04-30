class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print("first name : " + self.first_name)
        print("last name : " + self.last_name)
        print("age : " + str(self.age))
        print("location : " + self.location)

    def greet_user(self):
        print("Hello, " + str(self.first_name).title() + str(self.last_name).title() + '.')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Vincent', 'CHEN', 23, 'Beijing')
user.describe_user()
user.greet_user()
for i in range(1, 11):
    user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)