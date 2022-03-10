
# Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
# Click nbfs://nbhost/SystemFileSystem/Templates/Python/_empty_module.py to edit this template


# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("****************Python Simple Calculator****************")



while True:
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    print("Select operation.")
    print("+ Add")
    print("- Subtract")
    print("* Multiply")
    print("/ Divide")
    
    option = input("Enter choice(+ - * /): ")
    
    if option == '+':
        print("\nAddition is Selected!")
        print(num1 , "+", num2, " = ", add(num1, num2))
    
    elif option == '-':
        print("\nSubtraction is Selected!")
        print(num1 , "-", num2, " = ", subtract(num1, num2))
        
    elif option == '*':
        print("\nMultiplication is Selected!")
        print(num1 , "*", num2, " = ", multiply(num1, num2))
        
    elif option == '/':
        print("\nDivision is Selected!")
        print(num1 , "/", num2, " = ", divide(num1, num2))
        
    else:
        print("Invalid Input")
        
    repeatCalc = input("\nCalculate Again: Yes/no: ")
    if repeatCalc == "no" or repeatCalc == "n":
        break;

print("**********Program Terminated!**********")


