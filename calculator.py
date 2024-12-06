def arithmetic_calculator():
    print(" Arithmetic Calculator")
    print("Type 'exit' to quit the calculator.")
    
    while True:
        # Taking user input
        user_input = input("\nEnter your expression: ").strip() #.stript() is used to handle blank spaces. with .stript 2 + 3 and 2+3 are counted as the same
        # Exit condition
        if user_input.lower() == 'exit': # .lower() is used to handle expressions like: exit, Exit, eXit, EXit. it helps to recognize all the expressions as the same.
            print("Thank you for using Rafid's calculator. Goodbye!")
            break

        try:
            # Evaluate the expression
            # Use eval with a limited set of allowed operators
            result = eval(user_input, {"__builtins__": None}, # "eval" is a function that dynamically evaluates the user's input
            {
                "abs": abs, 
                "round": round,
                "pow": pow
            })
            print(f"Result: {result}")
        except (SyntaxError, NameError, ZeroDivisionError, TypeError) as e:
            print(f"Error: Invalid input. {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

# Run the calculator
arithmetic_calculator()
"""
The calculator supports:
*Basic Arithmetic operations:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Exponentiation (**)
Floor Division (//) this ignores the decimal part in a calculation
Modulus (%)
*Grouping with Parentheses:
Example: (2 + 3) * 4
*Safe Built-in Functions:
abs(x): Returns the absolute value of x.
round(x, n): Rounds x to n decimal places.
pow(x, y): x^n Computes

"""