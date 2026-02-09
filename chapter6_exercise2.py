'''
CIS 117 - Chapter 6 Exercise 2 - Erick Ramos

This program manages a dictionary of friends you've encountered in 2017 and 2018. 

The steps are as follows:

Creates a dictionary representing your friends that you met in 2017 and 2018. 
In this dictionary, use '2017' and '2018' as keys, with the respective lists of friends as values.
For example:
friend_dict = {'2017': ["Joe", "Lily"], '2018': ["Bob", "Tom"]}

Asks the user to enter the name of a friend.
Then, indicates whether you found the friend in 2017 or 2018.

Prompts the user to add a new friend's name to either the 2017 or 2018 lists. 
Be sure to ask the user for the year they want to associate with this friend's name.
Adds the entered friend's name to the appropriate list within the dictionary ('2017' or '2018').
Finally, prints the updated friends' dictionary on the screen.
'''


def get_friend_name():
    '''
    Function to ask the user to input the name of a friend
    '''
    friend_name = input("Enter the name of a friend: ")
    return friend_name


def get_friend_year(friend_name):
    '''
    Function to ask the user to input the year the friend was met
    '''
    friend_year = input(f"Enter the year you met {friend_name}: ")
    return friend_year


def main():
    '''
    Main program function to control friends list.
    '''
    
    # Create a dictionary representing your friends that you met in 2017 and 2018.
    friend_dict = {
        "2017": ["Elizabeth", "Gin"],
        "2018": ["Jimmy", "Benny"]
    }

    # Ask the user to enter the name of a friend
    friend_name = get_friend_name()

    # Indicate whether you found the friend in 2017 or 2018
    if friend_name in friend_dict["2017"]:
        print(f"You met {friend_name} in 2017")
    elif friend_name in friend_dict["2018"]:
        print(f"You met {friend_name} in 2018")
    else:
        print(f"Your friend {friend_name} was not found in either entry.")        

    # Prompt the user to add a new friend's name to either the 2017 or 2018 lists
    new_friend = get_friend_name()
    new_year = get_friend_year(new_friend)

    # Add the entered friend's name to the appropriate list within the dictionary
    if new_year in friend_dict:
        friend_dict[new_year].append(new_friend)
    else:
        print("The year needs to be 2017 or 2018")

    print("Look at all your friends!", friend_dict)

# Run the main function
main()


# Output 1
# Enter the name of a friend: Erick
# Your friend Erick was not found in either entry.
# Enter the name of a friend: Ramos
# Enter the year you met Ramos: 2017
# Look at all your friends! {'2017': ['Elizabeth', 'Gin', 'Ramos'], '2018': ['Jimmy', 'Benny']}


# Output 2
# Enter the name of a friend: Gin
# You met Gin in 2017
# Enter the name of a friend: Ellie
# Enter the year you met Ellie: 2018
# Look at all your friends! {'2017': ['Elizabeth', 'Gin'], '2018': ['Jimmy', 'Benny', 'Ellie']}