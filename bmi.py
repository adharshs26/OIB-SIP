def calculate_bmi(weight, height):
    """
    Calculate BMI using weight (kg) and height (m).
    """
    height = height/100
    try:
        # Calculate BMI
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        print("Height cannot be zero.")
        return None

def classify_bmi(bmi):
    """
    Classify BMI into categories.
    """
    if bmi is None:
        return "Invalid BMI"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """
    Main function to prompt user input and display BMI results.
    """
    print("Welcome to the BMI Calculator!")

    # Prompt user for weight and height
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (cm): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Classify BMI
        category = classify_bmi(bmi)
        
        # Display the results
        if bmi is not None:
            print(f"Your BMI is: {bmi:.2f}")
            print(f"BMI Category: {category}")

    except ValueError:
        print("Please enter valid numeric values for weight and height.")

if __name__ == "__main__":
    main()
