
##Calculation logic for BMR and TDEE.


from user_profile import UserProfile

class Calculator:
    @staticmethod
    def calculate_bmr(profile: UserProfile) -> float:
        """
        Calculates BMR using the Mifflin-St Jeor Equation.
        Formula:
          Men: (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
          Women: (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
        """
        profile.validate_inputs()
        
        base_calc = (10 * profile.weight_kg) + (6.25 * profile.height_cm) - (5 * profile.age)
        
        if profile.gender == 'male':
            return base_calc + 5
        else:
            return base_calc - 161
    @staticmethod
    def calculate_tdee(profile: UserProfile) -> float:
        """
        Calculates TDEE by multiplying BMR 
        by an activity level multiplier.
        """
        bmr = Calculator.calculate_bmr(profile)
        
        multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'extreme': 1.9
        }
        
        multiplier = multipliers.get(profile.activity_level, 1.2)
        return bmr * multiplier