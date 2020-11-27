import unittest

from models.mechanic import *
from models.car import *
from models.repair import *

class RepairTest(unittest.TestCase):

    def setUp(self):
        self.mechanic = Mechanic("Thomas", "Brown", True)
        self.car = Car("ZZ99NEW", "VW", "Golf", "2021-07-13")
        self.repair = Repair("2020-11-29", "Repaired puncture", self.mechanic, self.car)

    
    def test_repair_has_date(self):
        self.assertEqual("2020-11-29", self.repair.repair_date)
        
    def test_repair_has_details(self):
        self.assertEqual("Repaired puncture", self.repair.details)

    def test_repair_has_mechanic(self):
        self.assertEqual("Brown", self.repair.mechanic.last_name)

    def test_repair_has_car(self):
        self.assertEqual("ZZ99NEW", self.repair.car.registration_number)
    