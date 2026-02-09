'''
CIS 117 - Chapter 4 Exercise 2 - Erick Ramos

This program prompts the user for hours and rate per hour to compute gross pay.
Additionally, it gives the employee 1.5 times the hourly rate for hours worked above 40 hours.
It uses the isdigit method to handle non-numeric input gracefully.

Enter Hours: 20
Enter Rate: nine
Error, please enter a numeric input
Enter Hours: forty
Error, please enter a numeric input

Rewrite your code to validate the inputs and keep asking the user to enter valid inputs for the hours and the rate value.
So:
Ask the user for their company name
Ask the user for the hours they work in a week
Ask the user for the rate (dollar/hour)
Check user inputs
Do it in a loop
strip the inputs  => use strip()
If you use float() or int() functions, then you don't need to use strip().
However, if you want to use the isdigit() method, you may need to use strip() first.
Only display 2 decimal points when displaying all the numbers.  => use round(theOutput,2)
Print the company's name, the hours, the rate, and the gross pay, and also a random number between 1000 and 2000 for their document numbers.

Example output:
Enter your company name: Google
Enter the hours:   45
Enter the rate: 10
Print the company's name, the hours, the rate, and the gross pay, and also a random number between 1000 and 2000 for their document numbers.
Company: Google
hours: 45
Rate: 10
**********************************************
Your document number is: 1585
Your Google gross pay is 475 dollars.
'''
from random import randint


INPUT_PROMPT = "Enter your company name: "
ERROR_PROMPT = "Please enter a valid input"
HOURS_PROMPT = "Enter the hours: "
RATE_PROMPT = "Enter the rate: "


hours = 0
rate = 0
regular_hours = 40
overtime_multiplier = 1.5


valid_company = False
while not valid_company:
    company_input = input(INPUT_PROMPT)
    if company_input.isalnum():
        valid_company = True
        company = str(company_input)
    else:
        print(ERROR_PROMPT)


valid_hours = False
while not valid_hours:
    hours_input = input(HOURS_PROMPT)
    if hours_input.isdigit():
        valid_hours = True
        hours = float(hours_input)
    else:
        print(ERROR_PROMPT)


valid_rate = False
while not valid_rate:
    rate_input = input(RATE_PROMPT)
    if rate_input.isdigit():
        valid_rate = True
        rate = float(rate_input)
    else:
      print(ERROR_PROMPT)


if valid_hours and valid_rate:

    document_number = randint(1000,2000)

    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        overtime_hours = hours - regular_hours
        overtime_rate = rate * overtime_multiplier
        overtime_pay = overtime_hours * overtime_rate
        regular_pay = rate * regular_hours
        pay = regular_pay + overtime_pay
    
    print(f"\nCompany: {company}")
    print(f"Hours: {hours}")
    print(f"Rate: {rate}")
    print("**********************************************")
    print(f"Your document number is: {document_number}")
    print(f"Your {company} gross pay is {pay} dollars.")

else:
    print(ERROR_PROMPT)

# Output 1:

# Enter your company name: Google
# Enter the hours: test
# Please enter a valid input
# Enter the hours: forty
# Please enter a valid input
# Enter the hours: 45
# Enter the rate: ten
# Please enter a valid input
# Enter the rate: 10

# Company: Google
# Hours: 45.0
# Rate: 10.0
# **********************************************
# Your document number is: 1114
# Your Google gross pay is 475.0 dollars.


# Output 2:

# Enter your company name: Amazon
# Enter the hours: -45
# Please enter a valid input
# Enter the hours: 45
# Enter the rate: tes$5
# Please enter a valid input
# Enter the rate: 20

# Company: Amazon
# Hours: 45.0
# Rate: 20.0
# **********************************************
# Your document number is: 1623
# Your Amazon gross pay is 950.0 dollars.


# Output 3:

# Enter your company name: apple
# Enter the hours: 45
# Enter the rate: 10

# Company: apple
# Hours: 45.0
# Rate: 10.0
# **********************************************
# Your document number is: 1003
# Your apple gross pay is 475.0 dollars.