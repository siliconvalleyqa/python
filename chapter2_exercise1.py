'''
CIS 117 - Chapter 2 Exercise 1 - Erick Ramos

This program prompts the user for hours and rate per hour to compute gross pay.
'''

hours = 0
rate = 0

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
pay = hours * rate

print(f"Pay: {pay}")

'''
Output 1:
Enter Hours: 60
Enter Rate: 50
Pay: 3000.0

Output 2:
Enter Hours: 42.5
Enter Rate: 23.25
Pay: 988.125
'''