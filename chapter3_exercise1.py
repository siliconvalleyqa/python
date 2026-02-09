'''
CIS 117 - Chapter 3 Exercise 1 - Erick Ramos

This program prompts the user for hours and rate per hour to compute gross pay.

Additionally, it gives the employee 1.5 times the hourly rate for hours worked above 40 hours.
'''

hours = 0
rate = 0
regular_hours = 40
overtime_multiplier = 1.5

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

if hours <= 40:
    pay = hours * rate
elif hours > 40:
    overtime_hours = hours - regular_hours
    overtime_rate = rate * overtime_multiplier
    overtime_pay = overtime_hours * overtime_rate
    regular_pay = rate * regular_hours
    pay = regular_pay + overtime_pay

print(f"Pay: {pay}")

'''
Output 1:
Enter Hours: 45
Enter Rate: 50
Pay: 2375.0

Output 2:
Enter Hours: 60
Enter Rate: 99
Pay: 6930.0
'''