"""
Modern Scientific Calculator
Built with Python - Developed by Lemayian
"""

import math
import os

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display calculator banner"""
    print("=" * 50)
    print(" 🧮  MODERN SCIENTIFIC CALCULATOR  🧮")
    print("=" * 50)
    print()

def basic_operations():
    """Perform basic arithmetic operations"""
    print("\n📊 BASIC OPERATIONS")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Modulus (%)")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
            print(f"\n✅ {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\n✅ {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\n✅ {num1} × {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("\n❌ Error: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\n✅ {num1} ÷ {num2} = {result}")
        elif choice == '5':
            result = num1 ** num2
            print(f"\n✅ {num1} ^ {num2} = {result}")
        elif choice == '6':
            result = num1 % num2
            print(f"\n✅ {num1} mod {num2} = {result}")
        else:
            print("\n❌ Invalid choice!")
    except ValueError:
        print("\n❌ Error: Please enter valid numbers!")

def scientific_operations():
    """Perform scientific calculations"""
    print("\n🔬 SCIENTIFIC OPERATIONS")
    print("1. Square Root (√)")
    print("2. Square (x²)")
    print("3. Cube (x³)")
    print("4. Sine (sin)")
    print("5. Cosine (cos)")
    print("6. Tangent (tan)")
    print("7. Logarithm (log)")
    print("8. Natural Log (ln)")
    print("9. Factorial (!)")
    print("10. Absolute Value (|x|)")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        num = float(input("Enter number: "))
        
        if choice == '1':
            if num < 0:
                print("\n❌ Error: Cannot take square root of negative number!")
            else:
                result = math.sqrt(num)
                print(f"\n✅ √{num} = {result}")
        elif choice == '2':
            result = num ** 2
            print(f"\n✅ {num}² = {result}")
        elif choice == '3':
            result = num ** 3
            print(f"\n✅ {num}³ = {result}")
        elif choice == '4':
            result = math.sin(math.radians(num))
            print(f"\n✅ sin({num}°) = {result}")
        elif choice == '5':
            result = math.cos(math.radians(num))
            print(f"\n✅ cos({num}°) = {result}")
        elif choice == '6':
            result = math.tan(math.radians(num))
            print(f"\n✅ tan({num}°) = {result}")
        elif choice == '7':
            if num <= 0:
                print("\n❌ Error: Logarithm undefined for non-positive numbers!")
            else:
                result = math.log10(num)
                print(f"\n✅ log({num}) = {result}")
        elif choice == '8':
            if num <= 0:
                print("\n❌ Error: Natural log undefined for non-positive numbers!")
            else:
                result = math.log(num)
                print(f"\n✅ ln({num}) = {result}")
        elif choice == '9':
            if num < 0 or num != int(num):
                print("\n❌ Error: Factorial only works for non-negative integers!")
            else:
                result = math.factorial(int(num))
                print(f"\n✅ {int(num)}! = {result}")
        elif choice == '10':
            result = abs(num)
            print(f"\n✅ |{num}| = {result}")
        else:
            print("\n❌ Invalid choice!")
    except ValueError:
        print("\n❌ Error: Please enter a valid number!")
    except OverflowError:
        print("\n❌ Error: Number too large!")

def constants():
    """Display mathematical constants"""
    print("\n🔢 MATHEMATICAL CONSTANTS")
    print(f"π (Pi) = {math.pi}")
    print(f"e (Euler's number) = {math.e}")
    print(f"τ (Tau) = {math.tau}")
    print(f"∞ (Infinity) = {math.inf}")

def expression_calculator():
    """Evaluate mathematical expressions"""
    print("\n🧮 EXPRESSION CALCULATOR")
    print("Examples: 2+3*4, (5+3)/2, 2**3")
    print("Type 'back' to return to main menu")
    
    while True:
        expr = input("\nEnter expression: ")
        
        if expr.lower() == 'back':
            break
        
        try:
            # Safe evaluation (limited to math operations)
            result = eval(expr, {"__builtins__": None}, {
                "sin": math.sin, "cos": math.cos, "tan": math.tan,
                "sqrt": math.sqrt, "log": math.log, "log10": math.log10,
                "pi": math.pi, "e": math.e, "pow": pow, "abs": abs
            })
            print(f"✅ Result: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main calculator menu"""
    while True:
        clear_screen()
        print_banner()
        
        print("📋 MAIN MENU")
        print("1. Basic Operations")
        print("2. Scientific Operations")
        print("3. Expression Calculator")
        print("4. Mathematical Constants")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            basic_operations()
        elif choice == '2':
            scientific_operations()
        elif choice == '3':
            expression_calculator()
        elif choice == '4':
            constants()
        elif choice == '5':
            print("\n👋 Thanks for using the calculator!")
            print("Developed by Lemayian\n")
            break
        else:
            print("\n❌ Invalid choice! Please enter 1-5.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()