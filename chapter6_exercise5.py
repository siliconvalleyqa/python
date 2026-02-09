##
# CIS 117 - Chapter 6 Exercise 5 - Erick Ramos
#
# This program Calculates a pay stub for these companies:
# ["Amazon", "Apple", "Facebook", "Google", "Uber"]
#
# The program performs the following steps:
# - Prompts the user for their company
# - Displays the companies after the second failed attempt
# - Prompts the user for the rate and hours
# - Saves the input in a dictionary named theDict
# - For hours higher than 40, multiply the rate by 1.5 
# - Prints the paystub
#


COMPANYLIST = ["Amazon", "Apple", "Facebook", "Google", "Uber"]
OVERTIME_HOURS = 40
MAX_INVALID_TRIES = 2


def getInputs():
    '''
    This function asks the user for company, rate, and hours with validation.
    This function asks the user for a company to validate it with the database. 
    If the user enters invalid inputs (not in the database)
    after the second invalid input, show (print) the valid companies 
    Returns a dictionary with these values.
    '''
    invalid_tries = 0
   
    # Ask the user for their company to validate it based on the database list
    company = input("Enter the name of your company: ")

    while company not in COMPANYLIST:
        invalid_tries += 1
        print("Company is not valid.")
        if invalid_tries >= MAX_INVALID_TRIES:
            print("Valid companies are:", ", ".join(COMPANYLIST))
        company = input("Enter the name of your company: ")

    # Ask the user the rate and the hours and validate them to be numeric and positive
    rate_str = input("Enter your hourly rate: ")
    while not rate_str.isdigit() or int(rate_str) <= 0:
        print("Please enter a valid positive number.")
        rate_str = input("Enter your hourly rate: ")
    rate = int(rate_str)

    hours_str = input("Enter your hours worked: ")
    while not hours_str.isdigit() or int(hours_str) <= 0:
        print("Please enter a valid positive number.")
        hours_str = input("Enter your hours worked: ")
    hours = int(hours_str)

    the_dict = {"company_name": company, "rate": rate, "hours": hours}

    return the_dict


def computePay(theDict):
    '''
    This function computes pay with overtime consideration.
    Returns the updated dictionary with total pay.
    '''
    rate = theDict["rate"]
    hours = theDict["hours"]
    if hours > OVERTIME_HOURS:
        overtime = hours - OVERTIME_HOURS
        total_pay = OVERTIME_HOURS * rate + overtime * rate * 1.5
    else:
        total_pay = hours * rate
    theDict["total_pay"] = total_pay
    return theDict


def printPay(theDict):
    '''
    This function prints the pay stub based on the dictionary values.
    '''
    print("\n---- Pay Stub ----")
    print("Company:", theDict["company_name"])
    print("Hours Worked:", theDict["hours"])
    print("Hourly Rate: $", theDict["rate"])
    print("Total Pay: $", round(theDict["total_pay"], 2))


def payProcess():
    '''
    This function is to process all other functions to get inputs,
    calculate and print the pay stub
    '''
    theDict = getInputs()
    theDict = computePay(theDict)
    printPay(theDict)


if __name__ == '__main__':
    payProcess()



## Output 1
# Enter the name of your company: Apple
# Enter your hourly rate: -10
# Please enter a valid positive number.
# Enter your hourly rate: 10
# Enter your hours worked: -10
# Please enter a valid positive number.
# Enter your hours worked: 45

# --- Pay Stub ---
# Company: Apple
# Hours Worked: 45
# Hourly Rate: $ 10
# Total Pay: $ 475.0

## Output 2
# Enter the name of your company: TestCompany
# Company is not valid.
# Enter the name of your company: John Deere
# Company is not valid.
# Valid companies are: Amazon, Apple, Facebook, Google, Uber
# Enter the name of your company: Google
# Enter your hourly rate: 100
# Enter your hours worked: 60

# ---- Pay Stub ----
# Company: Google
# Hours Worked: 60
# Hourly Rate: $ 100
# Total Pay: $ 7000.0