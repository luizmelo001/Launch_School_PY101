#Welcome user and inform that the annual rate is 8%
print("Welcome to the monthly payment calculator.")

#function that ensures a valid input

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("That is not a valid number. Please try again.")

#returns the monthly payment
def loan_calc(loan_amount, annual_rate, duration):
    monthly_rate = annual_rate / 12 / 100
    monthly_payment = loan_amount * (monthly_rate / (1 - (1 + monthly_rate) **(-duration)))

    return round(monthly_payment, 2)

while True:
    #gather the necessary data to perform the monthly payment calculation
    l_amount = get_valid_input("Choose the loan amount: $")
    l_duration = get_valid_input("Choose the loan duration in months:")
    annual_rate = get_valid_input("Choose the annual interest rate:")

    #calculate the monthly payment
    total_loan = loan_calc(l_amount,annual_rate,l_duration) * l_duration

    #print monthly payment, the total amount with interest and the total interest
    print(f"Your monthly payment would be:{loan_calc(l_amount,annual_rate,l_duration)}")
    print(f"The total payment would be:{total_loan}")
    print(f"The total interest would be:{round(total_loan - l_amount, 2)}")

    print("Another calculation?")
    answer = input().lower()

    while True:
        if answer.startswith("n") or answer.startswith("y"):
            break
        print("Please enter 'y' or 'n'.")
        answer = input()

    if answer[0] == 'n':
        break
    else:
        continue

print("Thank you for using the calculator!")