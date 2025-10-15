from core.calculator import Calculator

def add() -> None:
    print("\n============== ADD ==============")
    print("\n----ENTER TWO NUMBERS TO ADD----\n")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    calc = Calculator()
    print(f"{num_1} + {num_2} = {calc.add(num_1, num_2)}")

def subtract() -> None:
    print("\n============== SUBTRACT ==============")
    print("\n----ENTER TWO NUMBERS TO SUBTRACT----\n")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    calc = Calculator()
    print(f"{num_1} - {num_2} = {calc.subtract(num_1, num_2)}")

def multiplication() -> None:
    print("\n============== MULTIPLICATION ==============")
    print("\n----ENTER TWO NUMBERS TO MULTIPLY THEM----\n")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    calc = Calculator()
    print(f"{num_1} * {num_2} = {calc.multiply(num_1, num_2)}")

def divide() -> None:
    print("\n============== DIVIDE ==============")
    print("\n----ENTER TWO NUMBERS TO SPLIT THEM----\n")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    calc = Calculator()
    print(f"{num_1} / {num_2} = {calc.divide(num_1, num_2)}")

def exponentiaton() -> None:
    print("\n============== EXPONENTIATION ==============")
    print("\n----ENTER A BASE AND AN EXPONENT----\n")
    num_1 = float(input("Enter the base: "))
    num_2 = float(input("Enter the exponent: "))
    calc = Calculator()
    print(f"{num_1} ** {num_2} = {calc.power(num_1, num_2)}")

def root() -> None:
    print("\n============== NTH ROOT ==============")
    print("\n----ENTER A RADICAL AND INDEX----\n")
    num_1 = float(input("Enter the radical: "))
    num_2 = float(input("Enter the index: "))
    calc = Calculator()
    print(f"root {num_2} of {num_1} = {calc.root(num_1, num_2):2f}")

def square_root() -> None:
    print("\n============== SQUARE ROOT ==============")
    print("\n----ENTER A NUMBER TO GET ITS SQUARE ROOT----\n")
    num = float(input("Enter the positive number: "))
    calc = Calculator()
    print(f"The square root of {num} = {calc.square_root(num):2f}")

def logarithm() -> None:
    print("\n============== LOGARITHM ==============")
    print("\n----ENTER A ARGUMENT AND A BASE----\n")
    num_1 = float(input("Enter the argument: "))
    num_2 = float(input("Enter the base: "))
    calc = Calculator()
    print(f"Logarithm of {num_1} in base {num_2} = {calc.logarithm(num_1, num_2):2f}")

def factorial() -> None:
    print("\n============== FACTORIAL ==============")
    print("\n----ENTER A POSITIVE INTEGER----\n")
    num = int(input("Enter the number (number > 0): "))
    calc = Calculator()
    print(f"The factorial of {num} = {calc.factorial(num):2f}")

def absolute() -> None:
    print("\n============== ABSOLUTE VALUE ==============")
    print("\n----ENTER A NUMBER TO GET ITS ABSOLUTE VALUE----\n")
    num = float(input("Enter the number: "))
    calc = Calculator()
    print(f"The absolute value of {num} = {calc.absolute(num):2f}")

def module() -> None:
    print("\n============== MODULO ==============")
    print("\n----ENTER TWO NUMBERS TO GET YOUR REST----\n")
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    calc = Calculator()
    print(f"{num_1} % {num_2} = {calc.modulo(num_1, num_2):2f}")

def percentage() -> None:
    print("\n============== PERCENTAGE ==============")
    print("\n----ENTER THE PERCENTAGE AND NUMBER TO GET IT----\n")
    num_1 = float(input("Enter the percent: "))
    num_2 = float(input("Enter the number: "))
    calc = Calculator()
    print(f"The {num_1} percent of {num_2} = {calc.percentage(num_1, num_2):2f}")

def pause() -> None:
    input("\nPress ENTER to continue..\n")

def main():
    while True:
        print("============= CALCULATOR =============")
        print("What operation do you want to perform?")
        print("      1. Add")
        print("      2. Subtract")
        print("      3. Multiplication")
        print("      4. Divide")
        print("      5. Exponentiation")
        print("      6. Nth root")
        print("      7. Square root")
        print("      8. Logarithm")
        print("      9. Factorial")
        print("      10. Absolute value")
        print("      11. Modulus")
        print("      12. Percentage")
        print("      13. Salir")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                add()
                pause()
            elif choice == "2":
                subtract()
                pause()
            elif choice == "3":
                multiplication()
                pause()
            elif choice == "4":
                divide()
                pause()
            elif choice == "5":
                exponentiaton()
                pause()
            elif choice == "6":
                root()
                pause()
            elif choice == "7":
                square_root()
                pause()
            elif choice == "8":
                logarithm()
                pause()
            elif choice == "9":
                factorial()
                pause()
            elif choice == "10":
                absolute()
                pause()
            elif choice == "11":
                module()
                pause()
            elif choice == "12":
                percentage()
                pause()
            elif choice == "13":
                print("bye")
                break
            else:
                print("Invalid opcion. Try again..")
                pause()
        except Exception as e:
            print(f"Error: {e}")