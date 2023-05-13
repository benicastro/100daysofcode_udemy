"""Calculator Program, by Benedict Castro benedict.castro11@gmail.com
A digital computing tool.
Tags: short, code, math"""

# Import modules needed
import proj_art
import os

def main():
    print(proj_art.logo)
    print('''Milyastroc's Calculator, a digital computing tool.
            By Benedict Castro benedict.zcastro@gmail.com''')

    def ask_numbers(stage):
        if stage == "start":
            num1 = float(input("Please provide the first number: "))
            operation = input("What operation would you like?: \n + \t - \t * \t / \n Operation: ")
            num2 = float(input("Please provide the next number: "))
            return num1, num2, operation
        else:
            operation = input("What operation would you like?: \n + \t - \t * \t / \n Operation: ")
            num2 = float(input("Please provide the next number: "))
            return num2, operation

    def perform_operation(operation, num1, num2):
        """This function performs an arithmetic operation based on the input numbers."""

        # Define all arithmetic operations
        def add(num1, num2):
            return num1 + num2

        def subtract(num1, num2):
            return num1 - num2

        def multiply(num1, num2):
            return num1 * num2

        def divide(num1, num2):
            return num1 / num2

        # Create a dictionary containing these operations
        operation_dictionary = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }

        calculate = operation_dictionary[operation]
        return calculate(num1, num2)

    run_program = True
    while run_program:  # Main program loop
        stage = "start"
        num1, num2, operation = ask_numbers(stage)
        result = perform_operation(operation, num1, num2)
        print(f"{num1} {operation} {num2} = {result}")

        # Ask user if they want to continue calculating
        calculate_again = True
        while calculate_again:
            continue_calculation = input(f'Do you want to continue with the previous result ({result})?: Type "yes" or "no": ')
            if continue_calculation.lower() != "yes":
                os.system('cls' if os.name == 'nt' else 'clear')
                calculate_again = False
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                stage = "continuation"
                num1 = result
                num2, operation = ask_numbers(stage)
                result = perform_operation(operation, num1, num2)
                print(f"{num1} {operation} {num2} = {result}")

        # Ask the user if they want to run the calculator again
        use_again = input('Do you want to use the calculator again? Type "yes" or "no": ')
        if use_again.lower() != "yes":
            run_program = False
        os.system('cls' if os.name == 'nt' else 'clear')

    print("Thank you for using this tool. I hope you had a great time!")


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()
