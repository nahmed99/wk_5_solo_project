import unittest

from models.mechanic import *

class MechanicTest(unittest.TestCase):

    def setUp(self):
        self.mechanic_mot = Mechanic("Thomas", "Brown", True)
        self.mechanic_no_mot = Mechanic("Roger", "Rabbit", False)

    
    def test_mechanic_has_first_name(self):
        self.assertEqual("Thomas", self.mechanic_mot.first_name)
        
    def test_mechanic_has_second_name(self):
        self.assertEqual("Rabbit", self.mechanic_no_mot.last_name)


    def test_mechanic_is_mot_qualified(self):
        self.assertEqual(True, self.mechanic_mot.mot_qualified)
        
    def test_mechanic_is_not_mot_qualified(self):
        self.assertEqual(False, self.mechanic_no_mot.mot_qualified)

    

