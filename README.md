# Personal TDEE & Calorie Planning Calculator

## Project Description
The Personal TDEE & Calorie Planning Calculator is a Python-based software application designed to calculate an individual's estimated Total Daily Energy Expenditure (TDEE) based on personal body measurements, age, sex, and activity levels. It also provides tailored calorie targets (for maintenance, weight loss, or weight gain) and macro-nutrient breakdowns to support personal fitness and health goals.

## Purpose of the Application
The purpose of this project is twofold:
1. To provide a clean, reliable, and user-friendly CLI tool for calculating daily caloric and nutritional needs.
2. To serve as a complete, professional software engineering project demonstrating modern DevOps practices, version control, automated testing, and CI/CD pipelines.

## Planned Features
1. Personal profile input (Age, Sex, Height, Weight).
2. Basal Metabolic Rate (BMR) calculation using the Mifflin-St Jeor formula.
3. Activity level selection (Sedentary, Lightly active, Moderately active, Very active, Extra active).
4. Total Daily Energy Expenditure (TDEE) calculation.
5. Configurable weight-loss calorie deficit targets.
6. Configurable weight-gain calorie surplus targets.
7. Fitness goal selection (Maintenance, Weight loss, Weight gain).
8. Macronutrient calculations (Protein, Carbohydrates, Fats).
9. Calculation session history logging.
10. Robust input validation and error handling.

## Create and activate a Python virtual environment:
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate

## How to Run the Application
(Instructions will be updated as application modules are implemented)
python main.py

## How to Execute Tests
(Instructions will be updated when unit tests are implemented)
Bash
python -m unittest discover tests

## Project Administration & Team
Team Members: 1 (Solo Developer - Adaora Obialo)

## Working Hours:
 Monday to Friday, 9:00 AM – 5:00 PM

## Preferred Communication Channels: 
GitHub Issues, Email

## Code Review Policy & Development Rules
All feature development must take place on dedicated feature branches (following GitHub Flow).
Commits must strictly follow Semantic Commit Conventions.
Pull requests require self-review documentation and successful automated testing before merging into main.
No sensitive credentials or API keys will be committed to the repository.

## Technologies Used
* **Programming Language:** Python 3.14
* **Version Control:** Git & GitHub
* **Testing Framework:** Python `unittest`
* **CI/CD Automation:** GitHub Actions

## Installation Instructions
1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/Adaora101/tdee-calculator.git](https://github.com/Adaora101/tdee-calculator.git)
   cd tdee-calculator