"""
Enhanced Modern Scientific Calculator
Built with Python - Developed by Lemayian
"""

import math
import os
import json
import csv
from datetime import datetime
from collections import deque
from typing import List, Tuple, Optional

# Global variables for calculator state
calculation_history = deque(maxlen=100)
memory_store = 0.0
angle_mode = "deg"

# Try to import colorama for colored output
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False
    class Fore:
        GREEN = RED = BLUE = YELLOW = CYAN = MAGENTA = RESET = ""
    class Style:
        BRIGHT = DIM = RESET_ALL = ""

# Try to import requests for currency conversion
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Display calculator banner"""
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * 60}")
    print(f" 🧮  ENHANCED MODERN SCIENTIFIC CALCULATOR  🧮")
    print(f"{'=' * 60}{Style.RESET_ALL}")
    print()

def color_print(text: str, color: str = ""):
    """Print colored text if colorama is available"""
    print(f"{color}{text}{Fore.RESET}")

def add_to_history(expression: str, result: float):
    """Add calculation to history"""
    calculation_history.append({
        'expression': expression,
        'result': result,
        'timestamp': datetime.now().isoformat()
    })

# ============================================================================
# BASIC OPERATIONS
# ============================================================================

def basic_operations():
    """Perform basic arithmetic operations"""
    print(f"\n{Fore.BLUE}📊 BASIC OPERATIONS{Fore.RESET}")
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
        
        result = None
        expr_str = ""
        
        if choice == '1':
            result = num1 + num2
            expr_str = f"{num1} + {num2}"
        elif choice == '2':
            result = num1 - num2
            expr_str = f"{num1} - {num2}"
        elif choice == '3':
            result = num1 * num2
            expr_str = f"{num1} × {num2}"
        elif choice == '4':
            if num2 == 0:
                color_print("\n❌ Error: Cannot divide by zero!", Fore.RED)
                return
            result = num1 / num2
            expr_str = f"{num1} ÷ {num2}"
        elif choice == '5':
            result = num1 ** num2
            expr_str = f"{num1} ^ {num2}"
        elif choice == '6':
            result = num1 % num2
            expr_str = f"{num1} mod {num2}"
        else:
            color_print("\n❌ Invalid choice!", Fore.RED)
            return
        
        if result is not None:
            color_print(f"\n✅ {expr_str} = {result}", Fore.GREEN)
            add_to_history(expr_str, result)
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)

# ============================================================================
# SCIENTIFIC OPERATIONS
# ============================================================================

def scientific_operations():
    """Perform scientific calculations"""
    global angle_mode
    
    print(f"\n{Fore.MAGENTA}🔬 SCIENTIFIC OPERATIONS{Fore.RESET}")
    print(f"Current angle mode: {angle_mode.upper()}")
    print("1. Square Root (√)")
    print("2. Square (x²)")
    print("3. Cube (x³)")
    print("4. Sine (sin)")
    print("5. Cosine (cos)")
    print("6. Tangent (tan)")
    print("7. Arc Sine (asin)")
    print("8. Arc Cosine (acos)")
    print("9. Arc Tangent (atan)")
    print("10. Logarithm Base 10 (log)")
    print("11. Natural Logarithm (ln)")
    print("12. Factorial (!)")
    print("13. Absolute Value (|x|)")
    print("14. Ceiling (⌈x⌉)")
    print("15. Floor (⌊x⌋)")
    print("16. Toggle Angle Mode (deg/rad)")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    if choice == '16':
        angle_mode = "rad" if angle_mode == "deg" else "deg"
        color_print(f"\n✅ Angle mode changed to: {angle_mode.upper()}", Fore.GREEN)
        input("\nPress Enter to continue...")
        return
    
    try:
        num = float(input("Enter number: "))
        result = None
        expr_str = ""
        
        if choice in ['4', '5', '6']:
            angle_rad = math.radians(num) if angle_mode == "deg" else num
            angle_label = "°" if angle_mode == "deg" else " rad"
        elif choice in ['7', '8', '9']:
            angle_label = "°" if angle_mode == "deg" else " rad"
        else:
            angle_rad = None
            angle_label = ""
        
        if choice == '1':
            if num < 0:
                color_print("\n❌ Error: Cannot take square root of negative number!", Fore.RED)
                return
            result = math.sqrt(num)
            expr_str = f"√{num}"
        elif choice == '2':
            result = num ** 2
            expr_str = f"{num}²"
        elif choice == '3':
            result = num ** 3
            expr_str = f"{num}³"
        elif choice == '4':
            result = math.sin(angle_rad)
            expr_str = f"sin({num}{angle_label})"
        elif choice == '5':
            result = math.cos(angle_rad)
            expr_str = f"cos({num}{angle_label})"
        elif choice == '6':
            result = math.tan(angle_rad)
            expr_str = f"tan({num}{angle_label})"
        elif choice == '7':
            if num < -1 or num > 1:
                color_print("\n❌ Error: asin domain is [-1, 1]!", Fore.RED)
                return
            result = math.asin(num)
            if angle_mode == "deg":
                result = math.degrees(result)
            expr_str = f"asin({num})"
        elif choice == '8':
            if num < -1 or num > 1:
                color_print("\n❌ Error: acos domain is [-1, 1]!", Fore.RED)
                return
            result = math.acos(num)
            if angle_mode == "deg":
                result = math.degrees(result)
            expr_str = f"acos({num})"
        elif choice == '9':
            result = math.atan(num)
            if angle_mode == "deg":
                result = math.degrees(result)
            expr_str = f"atan({num})"
        elif choice == '10':
            if num <= 0:
                color_print("\n❌ Error: log requires positive number!", Fore.RED)
                return
            result = math.log10(num)
            expr_str = f"log({num})"
        elif choice == '11':
            if num <= 0:
                color_print("\n❌ Error: ln requires positive number!", Fore.RED)
                return
            result = math.log(num)
            expr_str = f"ln({num})"
        elif choice == '12':
            if num < 0 or num != int(num):
                color_print("\n❌ Error: Factorial requires non-negative integer!", Fore.RED)
                return
            result = math.factorial(int(num))
            expr_str = f"{int(num)}!"
        elif choice == '13':
            result = abs(num)
            expr_str = f"|{num}|"
        elif choice == '14':
            result = math.ceil(num)
            expr_str = f"⌈{num}⌉"
        elif choice == '15':
            result = math.floor(num)
            expr_str = f"⌊{num}⌋"
        else:
            color_print("\n❌ Invalid choice!", Fore.RED)
            return
        
        if result is not None:
            color_print(f"\n✅ {expr_str} = {result}", Fore.GREEN)
            add_to_history(expr_str, result)
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)
    except Exception as e:
        color_print(f"\n❌ Error: {str(e)}", Fore.RED)

# ============================================================================
# ADVANCED OPERATIONS
# ============================================================================

def advanced_operations():
    """Perform advanced mathematical operations"""
    print(f"\n{Fore.YELLOW}🚀 ADVANCED OPERATIONS{Fore.RESET}")
    print("1. GCD (Greatest Common Divisor)")
    print("2. LCM (Least Common Multiple)")
    print("3. Permutation (nPr)")
    print("4. Combination (nCr)")
    print("5. Prime Number Check")
    print("6. Fibonacci Sequence")
    print("7. Sum of Series (1 to n)")
    print("8. Product of Series (1 to n)")
    print("9. Exponentiation (e^x)")
    print("10. Hyperbolic Sine (sinh)")
    print("11. Hyperbolic Cosine (cosh)")
    print("12. Hyperbolic Tangent (tanh)")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        if choice in ['1', '2', '3', '4']:
            n = int(input("Enter first number (n): "))
            r = int(input("Enter second number (r): "))
            
            if choice == '1':
                result = math.gcd(n, r)
                expr_str = f"GCD({n}, {r})"
            elif choice == '2':
                result = abs(n * r) // math.gcd(n, r) if n and r else 0
                expr_str = f"LCM({n}, {r})"
            elif choice == '3':
                if n < 0 or r < 0 or r > n:
                    color_print("\n❌ Error: Invalid values for permutation!", Fore.RED)
                    return
                result = math.perm(n, r)
                expr_str = f"P({n}, {r})"
            elif choice == '4':
                if n < 0 or r < 0 or r > n:
                    color_print("\n❌ Error: Invalid values for combination!", Fore.RED)
                    return
                result = math.comb(n, r)
                expr_str = f"C({n}, {r})"
        
        elif choice == '5':
            num = int(input("Enter number to check: "))
            if num < 2:
                color_print(f"\n✅ {num} is NOT a prime number", Fore.YELLOW)
            else:
                is_prime = all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1))
                if is_prime:
                    color_print(f"\n✅ {num} is a PRIME number", Fore.GREEN)
                else:
                    color_print(f"\n✅ {num} is NOT a prime number", Fore.YELLOW)
            return
        
        elif choice == '6':
            n = int(input("Enter number of terms: "))
            if n <= 0:
                color_print("\n❌ Error: Number of terms must be positive!", Fore.RED)
                return
            fib_seq = [0, 1]
            for i in range(2, n):
                fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
            print(f"\n✅ Fibonacci sequence ({n} terms):")
            print(fib_seq[:n])
            return
        
        elif choice == '7':
            n = int(input("Enter n: "))
            result = n * (n + 1) // 2
            expr_str = f"Sum(1 to {n})"
        
        elif choice == '8':
            n = int(input("Enter n: "))
            if n < 0:
                color_print("\n❌ Error: n must be non-negative!", Fore.RED)
                return
            result = math.factorial(n)
            expr_str = f"Product(1 to {n})"
        
        elif choice == '9':
            x = float(input("Enter exponent: "))
            result = math.exp(x)
            expr_str = f"e^{x}"
        
        elif choice == '10':
            x = float(input("Enter value: "))
            result = math.sinh(x)
            expr_str = f"sinh({x})"
        
        elif choice == '11':
            x = float(input("Enter value: "))
            result = math.cosh(x)
            expr_str = f"cosh({x})"
        
        elif choice == '12':
            x = float(input("Enter value: "))
            result = math.tanh(x)
            expr_str = f"tanh({x})"
        
        else:
            color_print("\n❌ Invalid choice!", Fore.RED)
            return
        
        if 'result' in locals() and 'expr_str' in locals():
            color_print(f"\n✅ {expr_str} = {result}", Fore.GREEN)
            add_to_history(expr_str, result)
    
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)
    except Exception as e:
        color_print(f"\n❌ Error: {str(e)}", Fore.RED)

# ============================================================================
# EQUATION SOLVER
# ============================================================================

def equation_solver():
    """Solve quadratic and linear equations"""
    print(f"\n{Fore.GREEN}🧮 EQUATION SOLVER{Fore.RESET}")
    print("1. Linear Equation (ax + b = 0)")
    print("2. Quadratic Equation (ax² + bx + c = 0)")
    print("3. System of 2 Linear Equations")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        if choice == '1':
            print("\nSolve: ax + b = 0")
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            
            if a == 0:
                color_print("\n❌ Error: 'a' cannot be zero!", Fore.RED)
                return
            
            x = -b / a
            color_print(f"\n✅ Solution: x = {x}", Fore.GREEN)
            add_to_history(f"{a}x + {b} = 0", x)
        
        elif choice == '2':
            print("\nSolve: ax² + bx + c = 0")
            a = float(input("Enter a: "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            
            if a == 0:
                color_print("\n❌ Error: 'a' cannot be zero for quadratic!", Fore.RED)
                return
            
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
                color_print(f"\n✅ Two real solutions:", Fore.GREEN)
                print(f"   x₁ = {x1}")
                print(f"   x₂ = {x2}")
                add_to_history(f"{a}x² + {b}x + {c} = 0", x1)
            elif discriminant == 0:
                x = -b / (2*a)
                color_print(f"\n✅ One real solution: x = {x}", Fore.GREEN)
                add_to_history(f"{a}x² + {b}x + {c} = 0", x)
            else:
                real_part = -b / (2*a)
                imag_part = math.sqrt(abs(discriminant)) / (2*a)
                color_print(f"\n✅ Two complex solutions:", Fore.GREEN)
                print(f"   x₁ = {real_part} + {imag_part}i")
                print(f"   x₂ = {real_part} - {imag_part}i")
        
        elif choice == '3':
            print("\nSolve system:")
            print("a₁x + b₁y = c₁")
            print("a₂x + b₂y = c₂")
            a1 = float(input("Enter a₁: "))
            b1 = float(input("Enter b₁: "))
            c1 = float(input("Enter c₁: "))
            a2 = float(input("Enter a₂: "))
            b2 = float(input("Enter b₂: "))
            c2 = float(input("Enter c₂: "))
            
            det = a1*b2 - a2*b1
            
            if det == 0:
                color_print("\n❌ Error: System has no unique solution!", Fore.RED)
                return
            
            x = (c1*b2 - c2*b1) / det
            y = (a1*c2 - a2*c1) / det
            
            color_print(f"\n✅ Solution:", Fore.GREEN)
            print(f"   x = {x}")
            print(f"   y = {y}")
            add_to_history(f"System: x={x}, y={y}", x)
        
        else:
            color_print("\n❌ Invalid choice!", Fore.RED)
    
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)
    except Exception as e:
        color_print(f"\n❌ Error: {str(e)}", Fore.RED)

# ============================================================================
# CONVERSIONS
# ============================================================================

def conversion_operations():
    """Perform unit conversions"""
    print(f"\n{Fore.CYAN}🔄 UNIT CONVERSIONS{Fore.RESET}")
    print("1. Temperature (°C ↔ °F ↔ K)")
    print("2. Length (m ↔ ft ↔ in)")
    print("3. Weight (kg ↔ lb ↔ oz)")
    print("4. Speed (km/h ↔ mph ↔ m/s)")
    print("5. Area (m² ↔ ft² ↔ acre)")
    print("6. Volume (L ↔ gal ↔ ml)")
    print("7. Time (s ↔ min ↔ hr)")
    print("8. Data (B ↔ KB ↔ MB ↔ GB)")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        if choice == '1':
            print("\n1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            sub = input("Choose: ")
            val = float(input("Enter value: "))
            
            if sub == '1':
                result = (val * 9/5) + 32
                print(f"\n✅ {val}°C = {result}°F")
            elif sub == '2':
                result = (val - 32) * 5/9
                print(f"\n✅ {val}°F = {result}°C")
            elif sub == '3':
                result = val + 273.15
                print(f"\n✅ {val}°C = {result}K")
            elif sub == '4':
                result = val - 273.15
                print(f"\n✅ {val}K = {result}°C")
        
        elif choice == '2':
            print("\n1. Meters to Feet")
            print("2. Feet to Meters")
            print("3. Meters to Inches")
            print("4. Inches to Meters")
            sub = input("Choose: ")
            val = float(input("Enter value: "))
            
            if sub == '1':
                result = val * 3.28084
                print(f"\n✅ {val}m = {result}ft")
            elif sub == '2':
                result = val / 3.28084
                print(f"\n✅ {val}ft = {result}m")
            elif sub == '3':
                result = val * 39.3701
                print(f"\n✅ {val}m = {result}in")
            elif sub == '4':
                result = val / 39.3701
                print(f"\n✅ {val}in = {result}m")
        
        elif choice == '3':
            print("\n1. Kilograms to Pounds")
            print("2. Pounds to Kilograms")
            print("3. Kilograms to Ounces")
            sub = input("Choose: ")
            val = float(input("Enter value: "))
            
            if sub == '1':
                result = val * 2.20462
                print(f"\n✅ {val}kg = {result}lb")
            elif sub == '2':
                result = val / 2.20462
                print(f"\n✅ {val}lb = {result}kg")
            elif sub == '3':
                result = val * 35.274
                print(f"\n✅ {val}kg = {result}oz")
        
        elif choice == '4':
            print("\n1. km/h to mph")
            print("2. mph to km/h")
            print("3. km/h to m/s")
            sub = input("Choose: ")
            val = float(input("Enter value: "))
            
            if sub == '1':
                result = val * 0.621371
                print(f"\n✅ {val}km/h = {result}mph")
            elif sub == '2':
                result = val / 0.621371
                print(f"\n✅ {val}mph = {result}km/h")
            elif sub == '3':
                result = val / 3.6
                print(f"\n✅ {val}km/h = {result}m/s")
        
        elif choice == '8':
            print("\n1. Bytes to KB")
            print("2. KB to MB")
            print("3. MB to GB")
            print("4. GB to MB")
            sub = input("Choose: ")
            val = float(input("Enter value: "))
            
            if sub == '1':
                result = val / 1024
                print(f"\n✅ {val}B = {result}KB")
            elif sub == '2':
                result = val / 1024
                print(f"\n✅ {val}KB = {result}MB")
            elif sub == '3':
                result = val / 1024
                print(f"\n✅ {val}MB = {result}GB")
            elif sub == '4':
                result = val * 1024
                print(f"\n✅ {val}GB = {result}MB")
    
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)

# ============================================================================
# MEMORY OPERATIONS
# ============================================================================

def memory_operations():
    """Memory store and recall operations"""
    global memory_store
    
    print(f"\n{Fore.MAGENTA}💾 MEMORY OPERATIONS{Fore.RESET}")
    print(f"Current Memory: {memory_store}")
    print("1. Store in Memory (MS)")
    print("2. Add to Memory (M+)")
    print("3. Subtract from Memory (M-)")
    print("4. Recall Memory (MR)")
    print("5. Clear Memory (MC)")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        if choice == '1':
            val = float(input("Enter value to store: "))
            memory_store = val
            color_print(f"\n✅ {val} stored in memory", Fore.GREEN)
        elif choice == '2':
            val = float(input("Enter value to add: "))
            memory_store += val
            color_print(f"\n✅ Memory = {memory_store}", Fore.GREEN)
        elif choice == '3':
            val = float(input("Enter value to subtract: "))
            memory_store -= val
            color_print(f"\n✅ Memory = {memory_store}", Fore.GREEN)
        elif choice == '4':
            color_print(f"\n✅ Memory: {memory_store}", Fore.GREEN)
        elif choice == '5':
            memory_store = 0.0
            color_print("\n✅ Memory cleared", Fore.GREEN)
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)

# ============================================================================
# STATISTICS
# ============================================================================

def statistics_operations():
    """Statistical calculations"""
    print(f"\n{Fore.BLUE}📈 STATISTICS{Fore.RESET}")
    print("1. Mean (Average)")
    print("2. Median")
    print("3. Mode")
    print("4. Standard Deviation")
    print("5. Variance")
    print("6. Range")
    print("0. Back to Main Menu")
    
    choice = input("\nEnter choice: ")
    
    if choice == '0':
        return
    
    try:
        nums_str = input("Enter numbers separated by spaces: ")
        nums = [float(x) for x in nums_str.split()]
        
        if not nums:
            color_print("\n❌ Error: No numbers entered!", Fore.RED)
            return
        
        if choice == '1':
            result = sum(nums) / len(nums)
            color_print(f"\n✅ Mean = {result}", Fore.GREEN)
        elif choice == '2':
            sorted_nums = sorted(nums)
            n = len(sorted_nums)
            if n % 2 == 0:
                result = (sorted_nums[n//2-1] + sorted_nums[n//2]) / 2
            else:
                result = sorted_nums[n//2]
            color_print(f"\n✅ Median = {result}", Fore.GREEN)
        elif choice == '3':
            from collections import Counter
            count = Counter(nums)
            max_count = max(count.values())
            modes = [k for k, v in count.items() if v == max_count]
            if len(modes) == len(nums):
                color_print("\n✅ No mode (all values unique)", Fore.YELLOW)
            else:
                color_print(f"\n✅ Mode = {modes}", Fore.GREEN)
            return
        elif choice == '4':
            mean = sum(nums) / len(nums)
            variance = sum((x - mean) ** 2 for x in nums) / len(nums)
            result = math.sqrt(variance)
            color_print(f"\n✅ Standard Deviation = {result}", Fore.GREEN)
        elif choice == '5':
            mean = sum(nums) / len(nums)
            result = sum((x - mean) ** 2 for x in nums) / len(nums)
            color_print(f"\n✅ Variance = {result}", Fore.GREEN)
        elif choice == '6':
            result = max(nums) - min(nums)
            color_print(f"\n✅ Range = {result}", Fore.GREEN)
    except ValueError:
        color_print("\n❌ Error: Please enter valid numbers!", Fore.RED)

# ============================================================================
# HISTORY OPERATIONS
# ============================================================================

def view_history():
    """View calculation history"""
    print(f"\n{Fore.CYAN}📜 CALCULATION HISTORY{Fore.RESET}")
    
    if not calculation_history:
        color_print("\n❌ No history available!", Fore.YELLOW)
        return
    
    print(f"\nLast {len(calculation_history)} calculations:")
    for i, calc in enumerate(reversed(calculation_history), 1):
        print(f"{i}. {calc['expression']} = {calc['result']}")
    
    print("\n1. Export to CSV")
    print("2. Export to JSON")
    print("3. Clear History")
    print("0. Back")
    
    choice = input("\nEnter choice: ")
    
    if choice == '1':
        export_history_csv()
    elif choice == '2':
        export_history_json()
    elif choice == '3':
        calculation_history.clear()
        color_print("\n✅ History cleared!", Fore.GREEN)

def export_history_csv():
    """Export history to CSV"""
    try:
        filename = f"calc_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['expression', 'result', 'timestamp'])
            writer.writeheader()
            writer.writerows(calculation_history)
        color_print(f"\n✅ History exported to {filename}", Fore.GREEN)
    except Exception as e:
        color_print(f"\n❌ Error exporting: {str(e)}", Fore.RED)

def export_history_json():
    """Export history to JSON"""
    try:
        filename = f"calc_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(list(calculation_history), f, indent=2)
        color_print(f"\n✅ History exported to {filename}", Fore.GREEN)
    except Exception as e:
        color_print(f"\n❌ Error exporting: {str(e)}", Fore.RED)

# ============================================================================
# MAIN MENU
# ============================================================================

def main_menu():
    """Display main menu and handle user input"""
    while True:
        clear_screen()
        print_banner()
        
        print(f"{Fore.YELLOW}MAIN MENU{Fore.RESET}")
        print("1. 📊 Basic Operations")
        print("2. 🔬 Scientific Operations")
        print("3. 🚀 Advanced Operations")
        print("4. 🔄 Unit Conversions")
        print("5. 💾 Memory Operations")
        print("6. 📈 Statistics")
        print("7. 📜 View History")
        print("8. ℹ️  About")
        print("9. ❌ Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            basic_operations()
        elif choice == '2':
            scientific_operations()
        elif choice == '3':
            advanced_operations()
        elif choice == '4':
            conversion_operations()
        elif choice == '5':
            memory_operations()
        elif choice == '6':
            statistics_operations()
        elif choice == '7':
            view_history()
        elif choice == '8':
            print(f"\n{Fore.CYAN}Enhanced Modern Scientific Calculator")
            print("Version 2.0")
            print("Developed by Lemayian")
            print("Python-based calculator with advanced features{Fore.RESET}")
        elif choice == '9':
            color_print("\n👋 Thank you for using the calculator!", Fore.CYAN)
            break
        else:
            color_print("\n❌ Invalid choice! Please try again.", Fore.RED)
        
        input("\nPress Enter to continue...")

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        color_print("\n\n👋 Calculator terminated by user.", Fore.YELLOW)
    except Exception as e:
        color_print(f"\n❌ An unexpected error occurred: {str(e)}", Fore.RED)