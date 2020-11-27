import unittest

from models.car import *

class CarTest(unittest.TestCase):

    def setUp(self):
        self.car = Car("ZZ99NEW", "VW", "Golf", "2021-07-13")
        self.car_2 = Car("TT33OLD", "VW", "Polo", "2021-01-27", 1)

    
    def test_car_has_registration_number(self):
        self.assertEqual("ZZ99NEW", self.car.registration_number)

    def test_car_has_make(self):
        self.assertEqual("VW", self.car.make)

    def test_car_has_model(self):
        self.assertEqual("Golf", self.car.model)

    def test_car_has_mot_renewal_date(self):
        self.assertEqual("2021-07-13", self.car.mot_renewal_date)

    def test_car_has_id_None(self):
        self.assertIsNone(self.car.id)

    def test_car_has_id(self):
        self.assertEqual(1, self.car_2.id)
    