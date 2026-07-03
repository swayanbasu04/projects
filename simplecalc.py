def main():
    """Run a simple calculator until the user exits."""
    while True:
        print("\n1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("5 - Remainder")
        print("6 - Exit")

        try:
            option = int(input("Choose an operation (1-6): "))
        except ValueError:
            print("Invalid input. Enter a number between 1 and 6.")
            continue

        if option == 6:
            print("Exiting calculator. Goodbye!")
            break

        if option not in [1, 2, 3, 4, 5]:
            print("Invalid option! Choose between 1 and 6.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number entered!")
            continue

        try:
            if option == 1:
                result = num1 + num2
            elif option == 2:
                result = num1 - num2
            elif option == 3:
                result = num1 * num2
            elif option == 4:
                result = num1 / num2
            elif option == 5:
                result = num1 % num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            continue

        print("The calculated result is:", result)


if __name__ == "__main__":
    main()





    
      
