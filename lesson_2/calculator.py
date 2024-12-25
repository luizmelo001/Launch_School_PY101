# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

print("Welcome to Calculator!")

print("What is the first number?")
number1 = int(input())
print("What's the second number?")
number2 = int(input())

print(f"{number1} {number2}")

print('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

match operation:
    case "1": 
        output = number1 + number2
    case "2":
        output = number1 - number2
    case "3":
        output = number1 * number2
    case "4":
        output = number1 / number2
    case _:
        print("That is not a valid choice.") 

print(f"The result is: {output}")