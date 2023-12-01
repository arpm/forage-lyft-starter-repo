from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

import unittest
from datetime import datetime

class TestNubbinBattery(unittest.TestCase):
    def test_nubbin_battery_needs_service_true(self):
        today = datetime.now().date()
        five_years_ago = today.replace(year=today.year - 5)
        battery = NubbinBattery(last_service_date=five_years_ago, current_date=today)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_needs_service_false(self):
        today = datetime.now().date()
        three_years_ago = today.replace(year=today.year - 3)
        battery = NubbinBattery(last_service_date=three_years_ago, current_date=today)
        self.assertFalse(battery.needs_service())

class TestSpindlerBattery(unittest.TestCase):
    def test_spindler_battery_needs_service_true(self):
        today = datetime.now().date()
        three_years_ago = today.replace(year=today.year - 3)
        battery = SpindlerBattery(last_service_date=three_years_ago, current_date=today)
        self.assertTrue(battery.needs_service())

    def test_spindler_battery_needs_service_false(self):
        today = datetime.now().date()
        six_months_ago = today.replace(month=today.month - 6)
        battery = SpindlerBattery(last_service_date=six_months_ago, current_date=today)
        self.assertFalse(battery.needs_service())
