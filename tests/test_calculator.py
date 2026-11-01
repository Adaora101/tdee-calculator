##Unit tests for calculator.py BMR and TDEE functions.

import unittest
from calculator import calculate_bmr

class TestCalculator(unittest.TestCase):
    
    def test_calculate_bmr_male(self):
        # Test BMR calculation for a male
        # Weight = 70 kg, Height = 175 cm, Age = 25, Sex = 'male'
        # Formula: (10 * 70) + (6.25 * 175) - (5 * 25) + 5 = 700 + 1093.75 - 125 + 5 = 1673.75
        bmr = calculate_bmr(70.0, 175.0, 25, 'male')
        self.assertAlmostEqual(bmr, 1673.75)

    def test_calculate_bmr_female(self):
        # Test BMR calculation for a female
        # Weight = 60 kg, Height = 165 cm, Age = 30, Sex = 'female'
        # Formula: (10 * 60) + (6.25 * 165) - (5 * 30) - 161 = 600 + 1031.25 - 150 - 161 = 1320.25
        bmr = calculate_bmr(60.0, 165.0, 30, 'female')
        self.assertAlmostEqual(bmr, 1320.25)

    def test_calculate_bmr_invalid_sex(self):
        # Test that an invalid sex string raises a ValueError
        with self.assertRaises(ValueError):
            calculate_bmr(70.0, 175.0, 25, 'other')

if __name__ == '__main__':
    unittest.main()