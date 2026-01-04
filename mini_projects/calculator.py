# ===== Functions for calculator =====
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def product(num1, num2):
    return num1 * num2

def quotient(num1, num2):
    # Handle division by zero
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

# ===== User input =====
operation = input("Which operation do you want to perform? +, -, *, / : ").strip()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# ===== Perform calculation =====
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = product(num1, num2)
elif operation == '/':
    result = quotient(num1, num2)
else:
    result = "Invalid operation!"

# ===== Show result =====
print(f"The result of {num1} {operation} {num2} is: {result}")
