import unittest
from user_profile import UserProfile

class TestUserProfile(unittest.TestCase):
    def test_valid_profile_creation(self):
        profile = UserProfile(age=25, weight_kg=70.0, height_cm=175.0, gender="male", activity_level="moderate")
        self.assertTrue(profile.validate_inputs())

    def test_invalid_age(self):
        profile = UserProfile(age=150, weight_kg=70.0, height_cm=175.0, gender="male", activity_level="moderate")
        with self.assertRaises(ValueError):
            profile.validate_inputs()

    def test_invalid_gender(self):
        profile = UserProfile(age=25, weight_kg=70.0, height_cm=175.0, gender="robot", activity_level="moderate")
        with self.assertRaises(ValueError):
            profile.validate_inputs()

if __name__ == '__main__':
    unittest.main()