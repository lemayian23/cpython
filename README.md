# 🐍 Modern Python Calculator

A feature-rich scientific calculator built with Python. Supports basic arithmetic, scientific operations, expression evaluation, and mathematical constants.

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- 🔢 **Basic Operations** - Addition, subtraction, multiplication, division, power, modulus
- 🔬 **Scientific Functions** - Trigonometry (sin, cos, tan), logarithms, square root, factorial
- 🧮 **Expression Calculator** - Evaluate complex mathematical expressions
- 📐 **Mathematical Constants** - π (pi), e (Euler's number), τ (tau)
- ✅ **Error Handling** - Graceful handling of invalid inputs and operations
- 🎨 **Clean Interface** - User-friendly menu-driven terminal interface

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/lemayian23/python-calculator.git
cd python-calculator
```

2. Run the calculator:
```bash
python calculator.py
```

That's it! No external dependencies required (uses only Python standard library).

## 📖 Usage Guide

### Main Menu
When you run the calculator, you'll see:
```
=================================================
 🧮  MODERN SCIENTIFIC CALCULATOR  🧮
=================================================

📋 MAIN MENU
1. Basic Operations
2. Scientific Operations
3. Expression Calculator
4. Mathematical Constants
5. Exit
```

### Basic Operations
- **Addition**: Add two numbers
- **Subtraction**: Subtract two numbers
- **Multiplication**: Multiply two numbers
- **Division**: Divide (with zero-division protection)
- **Power**: Calculate x^y
- **Modulus**: Find remainder of division

### Scientific Operations
- **Square Root (√)**: Calculate √x
- **Square (x²)**: Calculate x²
- **Cube (x³)**: Calculate x³
- **Trigonometry**: sin, cos, tan (in degrees)
- **Logarithms**: log₁₀(x) and ln(x)
- **Factorial**: Calculate n! for non-negative integers
- **Absolute Value**: |x|

### Expression Calculator
Evaluate complex expressions like:
```
2+3*4          → 14
(5+3)/2        → 4.0
2**3           → 8
sqrt(16)       → 4.0
sin(30)*2      → 1.0
```

Available functions in expressions:
- `sin()`, `cos()`, `tan()`
- `sqrt()`, `log()`, `log10()`
- `pi`, `e` (constants)
- `pow()`, `abs()`

## 🎯 Example Usage

```python
# Basic calculation
Enter your choice (1-5): 1
Enter choice: 1
Enter first number: 15
Enter second number: 7
✅ 15.0 + 7.0 = 22.0

# Scientific calculation
Enter your choice (1-5): 2
Enter choice: 1
Enter number: 16
✅ √16.0 = 4.0

# Expression evaluation
Enter your choice (1-5): 3
Enter expression: 2**3 + sqrt(16)
✅ Result: 12.0
```

## 🛠️ Technical Details

### Built With
- **Python 3** - Core programming language
- **math module** - Standard library for mathematical operations
- **os module** - For cross-platform screen clearing

### Code Structure
```python
calculator.py
├── main()                    # Main menu loop
├── basic_operations()        # Arithmetic operations
├── scientific_operations()   # Scientific calculations
├── expression_calculator()   # Expression evaluator
├── constants()              # Display math constants
├── print_banner()           # UI banner
└── clear_screen()           # Terminal clearing
```

### Error Handling
The calculator handles:
- ✅ Division by zero
- ✅ Invalid number inputs
- ✅ Negative square roots
- ✅ Factorial of non-integers
- ✅ Logarithm of non-positive numbers
- ✅ Expression syntax errors
- ✅ Overflow errors

## 🎓 Learning Concepts

This project demonstrates:
- **Functions** - Code organization and reusability
- **Loops** - Menu system with `while` loops
- **Conditionals** - Decision making with `if/elif/else`
- **Exception Handling** - `try/except` blocks
- **Math Module** - Using Python standard library
- **User Input/Output** - Interactive terminal application
- **String Formatting** - f-strings for output

## 🔮 Future Enhancements

Potential features to add:
- [ ] GUI interface with Tkinter
- [ ] Calculation history
- [ ] Unit conversions
- [ ] Matrix operations
- [ ] Equation solver
- [ ] Graphing capabilities
- [ ] Save/load calculations

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**Developed by Lemayian**

## 🙏 Acknowledgments

- Built as a Python learning project
- Uses Python's powerful `math` module
- Inspired by scientific calculators

---

**⭐ If you find this project useful, please consider giving it a star!**

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions

---

Made with ❤️ and Python