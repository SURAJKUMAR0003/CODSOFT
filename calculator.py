def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a % b
def power(a, b):    return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    print("========================================")
    print("         SIMPLE CALCULATOR              ")
    print("========================================")

    while True:
        print("\n  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (*)")
        print("  4. Division       (/)")
        print("  5. Modulus        (%)")
        print("  6. Power          (^)")
        print("  7. Exit")

        choice = input("\nSelect operation (1-7): ").strip()

        if choice == "7":
            print("Goodbye!"); break

        if choice not in ["1","2","3","4","5","6"]:
            print("Invalid choice! Enter 1-7."); continue

        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        ops = {"1":(add,"+"), "2":(subtract,"-"), "3":(multiply,"*"),
               "4":(divide,"/"), "5":(modulus,"%"), "6":(power,"^")}

        func, symbol = ops[choice]
        result = func(a, b)

        print("\n----------------------------------------")
        if isinstance(result, str):
            print(f"  {result}")
        else:
            print(f"  {a} {symbol} {b} = {result}")
        print("----------------------------------------")

        again = input("\nCalculate again? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Goodbye!"); break

if __name__ == "__main__":
    main()
