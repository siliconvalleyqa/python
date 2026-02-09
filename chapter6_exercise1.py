'''
CIS 117 - Chapter 6 Exercise 1 - Erick Ramos

This program manages two lists of friends you've encountered in 2017 and 2018. 
These lists are represented as "friends_2017" and "friends_2018," respectively. 

The steps are as follows:

Creates two lists of friends you found in 2017 and 2018. For instance:
friends_2017 = ["Joe", "Lily"]
friends_2018 = ["Bob", "Tom"]

Concatenates the two lists into a single list, and then displays this combined list to the user.
 
Prompts the user to input the name of a friend.
Determines if the friend's name is found in either the 2017 or 2018 list, 
and provides feedback to the user accordingly. If the friend isn't found in either list, informs the user.
 
Requests the user to input the name of a new friend and the year (2017 or 2018) they want to associate with this friend.
Adds the new friend's name to the respective list (2017 or 2018).
 
Prints the updated 2017 and 2018 friends lists on the screen.
User inputs are not validated, and loops are not implemented.
'''


def print_list(input_list):
    '''
    Function to print the list passed as parameter input_list
    '''
    for item in input_list:
      print(item, end=" ")
    print()


def get_friend_name():
    '''
    Function to ask the user to input the name of a friend
    '''
    friend_name = input("Enter the name of a friend: ")
    return friend_name


def find_friend_name(name, input_list):
    '''
    Function that looks for the name in the list passed as input_list
    Returns True if found. Otherwise it returns False.
    '''
    if name in input_list:
        # print(f"Your friend {name} was found in position {input_list.index(name)}")
        return True
    else:
        # print(f"Your friend {name} is not in the list.")
        return False


def get_friend_year(friend_name):
    '''
    Function to ask the user to input the year the friend was met
    '''
    friend_year = int(input(f"Enter the year you met {friend_name}: "))
    return friend_year


def main():
    '''
    Main program function to control friends list.
    '''
    # Create two lists of friends you found in 2017 and 2018
    friends_2017 = ["Elizabeth", "Gin"]
    friends_2018 = ["Jimmy", "Benny"]

    # Concatenate the two lists into a single list
    all_friends = friends_2017 + friends_2018
    
    # Display this combined list to the user
    print("Your friends from 2017 and 2018 are: ")
    print_list(all_friends)

    # Prompt the user to input the name of a friend
    friend = get_friend_name()
   
    # Determine if the friend's name is found in either the 2017 or 2018 list, 
    # and provide feedback to the user accordingly. 
    # If the friend isn't found in either list, inform the user.
    friend_found_2017 = find_friend_name(friend, friends_2017)
    if friend_found_2017:
        # friend_found = False
        print(f"You met {friend} in 2017")
    
    friend_found_2018 = find_friend_name(friend, friends_2018)
    if friend_found_2018:
        # friend_found = False
        print(f"You met {friend} in 2018")
    
    if not friend_found_2017 and not friend_found_2018:
        print(f"Your friend {friend} was not found in either list.")

    # Request the user to input the name of a new friend 
    # and the year (2017 or 2018) they want to associate with this friend.
    new_friend = get_friend_name()
    new_friend_year = get_friend_year(new_friend)

    # Add the new friend's name to the respective list (2017 or 2018).
    if new_friend_year == 2017:
        friends_2017.append(new_friend)

    elif new_friend_year == 2018:
        friends_2018.append(new_friend)
    else:
        print("The year needs to be 2017 or 2018")

    # Print the updated 2017 and 2018 friends lists on the screen
    print("\n2017 Friends List")
    print_list(friends_2017)
    print("\n2018 Friends List")
    print_list(friends_2018)    


# Run the main function
main()


# Output 1
# Your friends from 2017 and 2018 are: 
# Elizabeth Gin Jimmy Benny Enter the name of a friend: Ramos
# Your friend Ramos was not found in either list.
# Enter the name of a friend: Ramos
# Enter the year you met Ramos: 2018


# 2017 Friends List
# Elizabeth Gin 

# 2018 Friends List
# Jimmy Benny Ramos


# Output 2
# Your friends from 2017 and 2018 are: 
# Elizabeth Gin Jimmy Benny 
# Enter the name of a friend: Jimmy
# You met Jimmy in 2018
# Enter the name of a friend: Duke
# Enter the year you met Duke: 2017

# 2017 Friends List
# Elizabeth Gin Duke 

# 2018 Friends List
# Jimmy Benny 