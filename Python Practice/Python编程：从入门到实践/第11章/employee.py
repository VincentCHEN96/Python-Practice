class Employee():
    '''Tested Class'''

    def __init__(self, first_name, last_name, annual_salary=0):
        '''init function'''

        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, increment=0):
        if int(increment) == 0:
            self.annual_salary += 5000
        else:
            self.annual_salary += int(increment)