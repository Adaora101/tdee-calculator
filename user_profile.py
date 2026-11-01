class UserProfile:
    def __init__(self, age: int, weight_kg: float, height_cm: float, gender: str, activity_level: str):
        self.age = age
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.gender = gender.lower()
        self.activity_level = activity_level.lower()

    def validate_inputs(self) -> bool:
        """Validates that user inputs fall within realistic bounds."""
        if self.age <= 0 or self.age > 120:
            raise ValueError("Age must be between 1 and 120 years.")
        if self.weight_kg <= 0 or self.weight_kg > 500:
            raise ValueError("Weight must be a positive value up to 500 kg.")
        if self.height_cm <= 0 or self.height_cm > 300:
            raise ValueError("Height must be between 1 and 300 cm.")
        if self.gender not in ['male', 'female']:
            raise ValueError("Gender must be 'male' or 'female'.")
        
        valid_activity_levels = ['sedentary', 'light', 'moderate', 'active', 'extreme']
        if self.activity_level not in valid_activity_levels:
            raise ValueError(f"Activity level must be one of {valid_activity_levels}.")
            
        return True