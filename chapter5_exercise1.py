
'''
CIS 117 - Chapter 5 Exercise 1 - Erick Ramos

This program prompts the user for hours and rate per hour to compute gross pay.
Additionally, it gives the employee 1.5 times the hourly rate for hours worked above 40 hours.

It validates numeric inputs
Enter Hours: 20
Enter Rate: nine
Error, please enter a numeric input
Enter Hours: forty 
Error, please enter a numeric input

The pay computation program uses the following functions: get_input, compute_pay, print_output
'''

def get_input():
    ERROR_PROMPT = "Please enter a valid input"
    HOURS_PROMPT = "Enter the hours: "
    RATE_PROMPT = "Enter the rate: "

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

    return (hours, rate)


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


def print_output(pay):
        print("**********************************************")
        print(f"Your gross pay is {pay} dollars.")


def main():

     the_hours, the_rate = get_input()
     the_pay = compute_pay(the_hours, the_rate)
     print_output(the_pay)

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