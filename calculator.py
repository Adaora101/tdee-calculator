
##Calculation logic for BMR and TDEE.


def calculate_bmr(weight_kg: float, height_cm: float, age: int, sex: str) -> float:
   
    base_bmr = (10 * weight_kg) + (6.25 * height_cm) - (5 * age)
    
    if sex.lower() == 'male':
        return base_bmr + 5
    elif sex.lower() == 'female':
        return base_bmr - 161
    else:
        raise ValueError("Sex must be either 'male' or 'female'.")