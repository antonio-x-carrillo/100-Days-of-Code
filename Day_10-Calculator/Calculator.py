from art import logo

# Create functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Store in functions in dictionary
calculations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

print(logo)
run_program = True
new_calc = True
first_number = 0.0
while run_program:
    if new_calc:
        first_number = float(input("What's the first number?: "))
    for symbol in calculations:
        print(symbol)
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = calculations[operation](first_number, second_number)
    print(f"{first_number} {operation} {second_number} = {result}")
    save_result = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type anything else to end the program: ").lower()
    if save_result == 'y':
        first_number = result
        new_calc = False
    elif save_result == 'n':
        new_calc = True
        print("\n"*20)
        print(logo)
    else:
        run_program = False
