
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