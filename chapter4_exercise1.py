'''
CIS 117 - Chapter 4 Exercise 1 - Erick Ramos

Ask the user to enter an email address.
Check that it is a valid email address 
=> it should have "@"  and "."  
(for example: if '@' and '.' in user_input:)
Find the domain name of the email address 
and print it for example, if a user entered 
joe@yahoo.com print "yahoo"
'''

INPUT_PROMPT = "Enter an email address: "
ERROR_PROMPT = "Invalid. Please enter a valid email"
valid_email = False

while not valid_email:
    user_input = input(INPUT_PROMPT)

    if '@' and "." in user_input:
        value = True
        split_email = user_input.split("@")
        domain_name = split_email[-1].split(".")
        print("Domain:", domain_name[0])
    else:
        print(ERROR_PROMPT)


'''

Output 1:
Enter an email address: invalid@gamil
Invalid. Please enter a valid email

Output 2:
Enter an email address: 12314
Invalid. Please enter a valid email

Output 3:
Enter an email address: @#$
Invalid. Please enter a valid email

Output 4:
Enter an email address: test@test.com
Domain: test
'''