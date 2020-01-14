from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        random_number = randint(1, self.sides)
        print(str(random_number))


die = Die()
for i in range(0, 10):
    die.roll_die()
print()

die = Die(10)
for i in range(0, 10):
    die.roll_die()
print()

die = Die(20)
for i in range(0, 10):
    die.roll_die()