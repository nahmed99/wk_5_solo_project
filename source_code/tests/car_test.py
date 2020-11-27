import unittest

from models.car import *

class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car("ZZ99NEW", "VW", "Golf", "2021-07-13")

    
    def test_car_has_registration_number(self):
        self.assertEqual("ZZ99NEW", self.car.registration_number)


    def test_car_has_make(self):
        self.assertEqual("VW", self.car.make)


    def test_car_has_model(self):
        self.assertEqual("Golf", self.car.model)


    def test_car_has_mot_renewal_date(self):
        self.assertEqual("2021-07-13", self.car.mot_renewal_date)
    