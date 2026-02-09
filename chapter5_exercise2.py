'''
CIS 117 - Chapter 5 Exercise 2 - Erick Ramos

This program prompts the user for hours and rate per hour to compute gross pay.
Additionally, it gives the employee 1.5 times the hourly rate for hours worked above 40 hours.
It uses the isdigit method to handle non-numeric input gracefully.

This program performs the following actions:
1. Ask the user for their company name (no need to validate the company name)
2. Ask the user for the hours they work in a week
3. Ask the user for the rate (dollar/hour)
4. Check user inputs (No need to validate the company name)
5. Do it in a loop
6. Only display 2 decimal points when displaying all the numbers.  => use round(theOutput,2)
7. Print the company's name, the hours, the rate, and the gross pay, and also a random number between 1000 to 2000 for their document numbers.
 
Example output:
Enter your company name: Google
Enter the hours:   45
Enter the rate: 10

Print the company's name, the hours, the rate, and the gross pay, and also a random number between 1000 to 2000 for their document numbers.

Company: Google
hours: 45
Rate: 10
**********************************************
Your document number is: 1585
Your Google gross pay is 475 dollars.

The pay computation program uses the following functions: get_input, compute_pay, print_output
'''
from random import randint

def get_input():
    INPUT_PROMPT = "Enter your company name: "
    ERROR_PROMPT = "Please enter a valid input"
    HOURS_PROMPT = "Enter the hours: "
    RATE_PROMPT = "Enter the rate: "

    company = input(INPUT_PROMPT)
    # Logic to validate company name, which is not needed
    # valid_company = False
    # while not valid_company:
    #     company_input = input(INPUT_PROMPT)
    #     if company_input.isalnum():
    #         valid_company = True
    #         company = str(company_input)
    #     else:
    #         print(ERROR_PROMPT)

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

    return (company, hours, rate)


def compute_pay(hours, rate):

    regular_hours = 40
    overtime_multiplier = 1.5

    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        overtime_hours = hours - regular_hours
        overtime_rate = rate * overtime_multiplier
        overtime_pay = overtime_hours * overtime_rate
        regular_pay = rate * regular_hours
        pay = regular_pay + overtime_pay

    return pay


def print_output(company, hours, rate, pay):
    
    document_number = randint(1000,2000)
    pay = round(pay,2)
    hours = round(hours, 2)
    rate = round(rate, 2)

    print(f"\nCompany: {company}")
    print(f"Hours: {hours}")
    print(f"Rate: {rate}")
    print("**********************************************")
    print(f"Your document number is: {document_number}")
    print(f"Your {company} gross pay is {pay} dollars.")

def main():

     the_company, the_hours, the_rate = get_input()
     the_pay = compute_pay(the_hours, the_rate)
     print_output(the_company,the_hours, the_rate, the_pay)

main()


# Output 1:
# Enter the hours: 45
# Enter the rate: 10
# **********************************************
# Your gross pay is 475.0 dollars.

# Output 2;
# Enter the hours: test
# Please enter a valid input
# Enter the hours: tem
# Please enter a valid input
# Enter the hours: 
# Please enter a valid input
# Enter the hours: tem
# Please enter a valid input
# Enter the hours: ten
# Please enter a valid input
# Enter the hours: -1
# Please enter a valid input
# Enter the hours: 40
# Enter the rate: test
# Please enter a valid input
# Enter the rate: test
# Please enter a valid input
# Enter the rate: -1
# Please enter a valid input
# Enter the rate: 10
# **********************************************
# Your gross pay is 400.0 dollars.

# Output 3:
# Enter the hours: -4
# Please enter a valid input
# Enter the hours: 40
# Enter the rate: -est
# Please enter a valid input
# Enter the rate: 100
# **********************************************
# Your gross pay is 4000.0 dollars.