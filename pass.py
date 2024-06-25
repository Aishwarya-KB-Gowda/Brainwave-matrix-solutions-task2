import re

def password_strength_check(password):
    # Initialize password strength score
    strength_score = 0

    # Check password length
    length = len(password)
    if length < 8:
        return "Very Weak"
    elif 8 <= length < 12:
        strength_score += 1
    elif 12 <= length < 16:
        strength_score += 2
    else:
        strength_score += 3

    # Check password complexity
    if re.search(r"[a-z]", password):
        strength_score += 1
    if re.search(r"[A-Z]", password):
        strength_score += 1
    if re.search(r"[0-9]", password):
        strength_score += 1
    if re.search(r"[!@#$%^&*()_+=-{}\[\]:;'\"<>,./?~`]", password):
        strength_score += 1

    # Map strength score to password strength level
    if strength_score == 1:
        return "Weak"
    elif strength_score == 2 or strength_score == 3:
        return "Medium"
    elif strength_score == 4:
        return "Strong"
    else:
        return "Very Strong"

def main():
    # Using input() to read the password for simplicity
    password = input("Enter a password: ")
    strength = password_strength_check(password)
    print(f"Password strength: {strength}")

if __name__ == "__main__":
    main()

