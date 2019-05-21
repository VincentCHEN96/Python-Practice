import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    '''To test the function of city_country'''

    def test_city_country(self):
        '''Testing function 1'''

        description = city_country('Beijing', 'China')
        self.assertEqual('Beijing, China', description)

    def test_city_country_population(self):
        '''Testing function 2'''

        description = city_country('Beijing', 'China', population=30000000)
        self.assertEqual('Beijing, China - population 30000000', description)


unittest.main()