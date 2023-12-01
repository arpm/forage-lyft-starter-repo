from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
import unittest

class TestCapuletEngine(unittest.TestCase):
    def test_capulet_engine_needs_service_true(self):
        engine = CapuletEngine(last_service_mileage=10000, current_mileage=42000)
        self.assertTrue(engine.needs_service())

    def test_capulet_engine_needs_service_false(self):
        engine = CapuletEngine(last_service_mileage=10000, current_mileage=23000)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_sternman_engine_needs_service_true(self):
        engine = SternmanEngine(warning_light_on=True)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_needs_service_false(self):
        engine = SternmanEngine(warning_light_on=False)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_willoughby_engine_needs_service_true(self):
        engine = WilloughbyEngine(last_service_mileage=3000, current_mileage=64000)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_needs_service_false(self):
        engine = WilloughbyEngine(last_service_mileage=3000, current_mileage=62000)
        self.assertFalse(engine.needs_service())
