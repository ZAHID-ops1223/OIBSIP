"""BMI Calculator - Command Line Version"""


def get_input(prompt):
    """Prompt user and validate that input is a positive number."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be positive. Please try again.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")


def calculate_bmi(weight, height):
    """Calculate BMI from weight (kg) and height (m)."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return classification based on BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 40)
    print("   BMI Calculator")
    print("=" * 40)

    weight = get_input("Enter your weight in kg: ")
    height = get_input("Enter your height in m: ")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI: {bmi:.2f}")
    print(f"Category: {category}")
    print("=" * 40)


if __name__ == "__main__":
    main()   