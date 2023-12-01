from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

import unittest

class TestCarriganTire(unittest.TestCase):
    def test_carrigan_tire_needs_service_true(self):
        wear = [0.1, 0.3, 0.6, 0.9]
        tire = CarriganTire(wear=wear)
        self.assertTrue(tire.needs_service())

    def test_carrigan_tire_needs_service_false(self):
        wear = [0.1, 0.3, 0.6, 0.8]
        tire = CarriganTire(wear=wear)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_octoprime_tire_needs_service_true(self):
        wear = [0.7, 0.7, 0.8, 0.9]
        tire = OctoprimeTire(wear=wear)
        self.assertTrue(tire.needs_service())

    def test_octoprime_tire_needs_service_false(self):
        wear = [0.6, 0.7, 0.7, 0.9]
        tire = OctoprimeTire(wear=wear)
        self.assertFalse(tire.needs_service())
