##Unit tests for calculator.py BMR and TDEE functions.

import unittest
from user_profile import UserProfile
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_bmr_male(self):
        profile = UserProfile(age=25, weight_kg=70.0, height_cm=175.0, gender="male", activity_level="moderate")
        # male: (10 * 70) + (6.25 * 175) - (5 * 25) + 5 = 1673.75
        bmr = Calculator.calculate_bmr(profile)
        self.assertAlmostEqual(bmr, 1673.75, places=2)

    def test_bmr_female(self):
        profile = UserProfile(age=30, weight_kg=60.0, height_cm=165.0, gender="female", activity_level="light")
        # female: (10 * 60) + (6.25 * 165) - (5 * 30) - 161 = 1320.25
        bmr = Calculator.calculate_bmr(profile)
        self.assertAlmostEqual(bmr, 1320.25, places=2)

if __name__ == '__main__':
    unittest.main()