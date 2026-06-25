import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    required = []

    if use_upper:
        chars += string.ascii_uppercase
        required.append(random.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        required.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += symbols
        required.append(random.choice(symbols))

    # Fill remaining length
    remaining = length - len(required)
    password_list = required + [random.choice(chars) for _ in range(remaining)]
    random.shuffle(password_list)
    return "".join(password_list)

def check_strength(length, use_upper, use_digits, use_symbols):
    score = sum([length >= 12, use_upper, use_digits, use_symbols])
    if score <= 1:   return "Weak ❌"
    elif score == 2: return "Medium ⚠"
    elif score == 3: return "Strong ✔"
    else:            return "Very Strong 🔒"

def main():
    print("========================================")
    print("        PASSWORD GENERATOR              ")
    print("========================================")

    while True:
        # Length input
        while True:
            try:
                length = int(input("\nEnter password length (4-64): "))
                if 4 <= length <= 64: break
                print("Length must be between 4 and 64.")
            except ValueError:
                print("Enter a valid number.")

        # Options
        use_upper   = input("Include Uppercase letters? (yes/no): ").strip().lower() in ["yes","y"]
        use_digits  = input("Include Numbers?           (yes/no): ").strip().lower() in ["yes","y"]
        use_symbols = input("Include Symbols?           (yes/no): ").strip().lower() in ["yes","y"]

        # How many passwords
        while True:
            try:
                count = int(input("How many passwords to generate? (1-10): "))
                if 1 <= count <= 10: break
                print("Enter a number between 1 and 10.")
            except ValueError:
                print("Enter a valid number.")

        print("\n========================================")
        print("       GENERATED PASSWORDS             ")
        print("========================================")
        for i in range(1, count+1):
            pwd = generate_password(length, use_upper, use_digits, use_symbols)
            print(f"  {i}. {pwd}")

        strength = check_strength(length, use_upper, use_digits, use_symbols)
        print(f"\n  Password Strength: {strength}")
        print("========================================")

        again = input("\nGenerate more passwords? (yes/no): ").strip().lower()
        if again not in ["yes","y"]:
            print("Goodbye!"); break

if __name__ == "__main__":
    main()
