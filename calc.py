#  - Demonstrable exposure and knowledge on the following areas, React, GraphQL, Javascript, REST API and Python.
#    - Knowledge and practical expertise on developing and rolling out solutions using the following languages: Javascript (React), Python
#    - Exposure to Microsoft Azure is a must

# Basic exercise on python

# phase 1. Build a simple calculator with the operations for SUM, Sustraction, division, power, multiplication of 2 numbers 
# phase 2. Handle Input of two numbers from an interface 


# Phase 1. The most simple calculator would have the 4 basic operations (+, -, /, x) 


# Define functions main and operations 
def sum(num1, num2):
    return num1 + num2

def sustract(num1, num2):
    return num1-num2

def multiply(num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1/num2


# Main function (Input: operation and values)

def main():
    # phase 2. Handle Input of two numbers from an interface 
    operation = input("Please enter the operation to execute (+, -, x, /):  ").strip()
    number1 = input("Please enter the first number: ")
    number2 = input("Please enter the second number: ")
    result = 0
    num1 = float(number1)
    num2 = float(number2)
    match operation:
        case '+':
          result = sum(num1, num2)
        case '-':
          result = sustract(num1, num2)
        case 'x':
          result = multiply(num1,num2)
        case '/':
          result = divide(num1, num2)
        case _:
          print('Invalid operation, try again using a known operator')

    print(result)

    tryagain=input('Try again? type Y, to quit type Q: ')
    if tryagain == 'Y' or tryagain == 'y' :
        main()
    else:
        return False
    

main()
