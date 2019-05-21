import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    '''Testing Class'''

    def setUp(self):
        self.employee = Employee('Vincent', 'CHEN', 250000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(255000, self.employee.annual_salary)

    def test_give_custom_raise(self):
        self.employee.give_raise(50000)
        self.assertEqual(300000, self.employee.annual_salary)


unittest.main()