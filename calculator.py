# ## Calculator

# A simple command-line calculator that performs basic arithmetic operations.

# ### Features
# - Addition, subtraction, multiplication, division  
# - Handles invalid input  
# - Prevents division by zero  
# - Allows continuous calculations  

# ### Tech Used
# - Python

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def calculator():
    print("=== Python Calculator ===")
    print("Operations: +  -  *  /")

    while True:
        try:
            a = float(input("\nEnter first number: "))
        except ValueError:
            print("Invalid number")
            continue

        while True:
            op = input("Enter operator (+, -, *, /): ")

            if op not in ['+', '-', '*', '/']:
                print("Invalid operator")
                continue

            try:
                b = float(input("Enter next number: "))
            except ValueError:
                print("Invalid number")
                continue

            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = sub(a, b)
            elif op == '*':
                result = mul(a, b)
            elif op == '/':
                result = div(a, b)

            print("Result:", result)

            # continue with result or reset
            choice = input("Continue with result? (y/n): ")
            if choice.lower() == 'y' and isinstance(result, float):
                a = result
            else:
                break

        again = input("\nStart new calculation? (y/n): ")
        if again.lower() != 'y':
            print("Exiting calculator...")
            break


if __name__ == "__main__":
    calculator()