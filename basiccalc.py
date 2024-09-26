# Program goal: To create very basic calculator
print("Welcome to the calculator app")

firstNumber = int(input("Enter in your first Number: "))
secondNumber = int(input("Enter in your second Number: "))

choice = input("A. Add, B. Subtract, C. Divide, D. Multiply: ")

if choice == "A":
    sum = firstNumber + secondNumber
    print(f"The sum of the 2 numbers is {sum}")
elif choice == "B":
    subtract = firstNumber - secondNumber
    print(f"The subtraction of the 2 numbers is {subtract}")
elif choice == "C":
    quotient = firstNumber / secondNumber
    print(f"The quotient of the 2 numbers is {quotient}")
elif choice == "D":
    product = firstNumber * secondNumber
    print(f"The product of the 2 numbers is {product}")
else:
    print("Bro didn't even enter one of the options try again")