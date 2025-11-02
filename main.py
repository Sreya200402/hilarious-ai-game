#console based calci using modules and "import"

#main.py (driver module)

import basic_calculation as basic
import advance_calculation as adv




def main():
    while True:
        print("\n===== Console Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulo")
        print("6. Square Root")
        print("7. Root (a ^ (1/b))")
        print("8. Exponent (a ^ b)")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '9':
            print("Exiting calculator. Goodbye!")
            break

        # Single number input (for sqrt)
        if choice == '6':
            x = float(input("Enter the number: "))
            print("Result:", adv.sqrt(x))
        
        # Two number inputs
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", basic.add(a, b))
            elif choice == '2':
                print("Result:", basic.sub(a, b))
            elif choice == '3':
                print("Result:", basic.mul(a, b))
            elif choice == '4':
                print("Result:", basic.div(a, b))
            elif choice == '5':
                print("Result:", basic.mod(a, b))
            elif choice == '7':
                print("Result:", adv.root(a, b))
            elif choice == '8':
                print("Result:", adv.expo(a, b))
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

