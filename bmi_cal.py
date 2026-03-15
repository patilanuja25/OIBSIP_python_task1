from datetime import datetime

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight", "You should eat a balanced diet."
    elif bmi < 25:
        return "Normal weight", "Great! Maintain your lifestyle."
    elif bmi < 30:
        return "Overweight", "Try regular exercise."
    else:
        return "Obese", "Consult doctor and plan fitness."


print("=== BMI Calculator ===")

name = input("Enter your name: ").strip()

while True:
    print("\n--- New Calculation ---")

    try:
        # Age validation
        age = int(input("Enter your age: "))
        if age <= 0:
            print("Age must be positive.")
            continue

        # Gender validation
        gender = input("Enter your gender (male/female): ").lower()
        if gender not in ["male", "female"]:
            print("Invalid gender. Enter 'male' or 'female'.")
            continue

        # Weight validation
        weight = float(input("Enter weight in kg: "))
        if weight <= 0:
            print("Weight must be positive.")
            continue

        # Height unit validation
        unit = input("Height unit (m/cm): ").lower()
        if unit not in ["m", "cm"]:
            print("Invalid unit. Please enter 'm' or 'cm'.")
            continue

        height = float(input("Enter height: "))
        if height <= 0:
            print("Height must be positive.")
            continue

        if unit == "cm":
            height = height / 100

        bmi = round(weight / (height * height), 2)
        category, tip = get_category(bmi)

        print("\n===== RESULT =====")
        print("Name:", name)
        print("Age:", age)
        print("Gender:", gender)
        print("BMI:", bmi)
        print("Category:", category)
        print("Health Tip:", tip)

        # Date & Time log
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save full record to file
        with open("bmi_history.txt", "a") as f:
            f.write("=====================================\n")
            f.write(f"Date & Time : {current_time}\n")
            f.write(f"Name        : {name}\n")
            f.write(f"Age         : {age}\n")
            f.write(f"Gender      : {gender}\n")
            f.write(f"Weight      : {weight} kg\n")
            f.write(f"Height      : {round(height,2)} m\n")
            f.write(f"BMI         : {bmi}\n")
            f.write(f"Category    : {category}\n")
            f.write(f"Health Tip  : {tip}\n")
            f.write("=====================================\n\n")

        print("Saved to bmi_history.txt")

    except ValueError:
        print("Invalid input — numbers only where required.")
        continue

    # Option to view history
    view = input("\nDo you want to see full BMI history? (y/n): ").lower()
    if view == "y":
        try:
            with open("bmi_history.txt", "r") as f:
                print("\n===== BMI HISTORY =====")
                print(f.read())
        except FileNotFoundError:
            print("No history found yet.")

    again = input("\nCalculate again? (y/n): ").lower()
    if again != "y":
        break


print("\nThank you for using BMI Calculator")