import re

def assess_password_strength(password):
    # Initialize criteria
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r'[A-Z]', password))
    lower_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Calculate the number of criteria met
    criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

    # Determine the strength of the password
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Provide feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lower_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one number.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character.")

    return strength, feedback

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter a password to assess: ").strip()

    strength, feedback = assess_password_strength(password)
    print(f"Password Strength: {strength}")
    
    if feedback:
        print("Feedback to improve your password:")
        for f in feedback:
            print(f"- {f}")

if __name__ == "__main__":
    main()