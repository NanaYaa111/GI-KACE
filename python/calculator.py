#lets build a simple calculator using functions

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def percentage(x, y):
    return (x / y) * 100
def power(x, y):
    return x ** y
def modulus(x, y):
    return x % y
def floor_divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x // y
def square_root(x):
    if x < 0:
        return "Error! Cannot compute square root of negative number."
    return x ** 0.5
def cube_root(x):
    if x < 0:
        return -(-x) ** (1/3)
    return x ** (1/3)
def factorial(x):
    if x < 0:
        return "Error! Factorial of negative number not defined."
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Percentage")
print("6. Power")
print("7. Modulus")
print("8. Floor Division")
print("9. Square Root")
print("10. Cube Root")
print("11. Factorial")    
while True:
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9/10/11):x ")
    if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == '5':
            print(f"{num1} % {num2} = {percentage(num1, num2)}")
        elif choice == '6':
            print(f"{num1} ^ {num2} = {power(num1, num2)}")
        elif choice == '7':
            print(f"{num1} % {num2} = {modulus(num1, num2)}")
        elif choice == '8': 
            print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
        elif choice == '9':
            print(f"Square root of {num1} = {square_root(num1)}")
        elif choice == '10':
            print(f"Cube root of {num1} = {cube_root(num1)}")
        elif choice == '11:':
            print(f"{int(num1)}! = {factorial(int(num1))}")
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    else:
        print("Invalid Input")
        
        
    
    
    