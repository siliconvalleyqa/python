##
# CIS 117 - Chapter 6 Exercise 4 - Erick Ramos
#
# This program displays a table for Figure Skating Medal Counts 
# - Creates a table for the medals
# - Prints the table.
# - Prints the total number of medals.
# - Prints the total number of gold, silver and bronze medals.
# - Removes countries without a gold medal from the table.
# - Prints the new table.
# - Uses dictionaries to save the data
# - Prints the dictionary with country as key and the value as a list
# - This part compares list vs. dictionaries to save data
#


def main(): 
    # Create a list of countries
    countries = [
        "Canada",
        "Italy",
        "Germany",
        "Japan",
        "Russia",
        "South Korea",
        "United States"
    ]

    # Create a table for the medals using nested lists
    counts = [
        [0, 3, 0],
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, 0],
        [3, 1, 1],
        [0, 1, 0],
        [1, 0, 1],
    ]

    # Print the table
    print("Table created for the medals:")
    print_table(counts)
    print()
    
    # Print the total number medals.
    total_medals = count_all_medals(counts)
    print(f"The total number of medals is {total_medals}")

    # Print the total number of gold, silver and bronze medals.
    gold_medals = count_medals_by_column(counts, 0)
    silver_medals = count_medals_by_column(counts, 1)
    bronze_medals = count_medals_by_column(counts, 2)

    print(f"The total number of gold medals is {gold_medals}")
    print(f"The total number of silver medals is {silver_medals}")
    print(f"The total number of bronze medals is {bronze_medals}")
    print()

    # Print the full table before editing
    print("Full Table with countries and totals:")
    print_table_totals(counts, countries)
    print()
    
    # Remove countries without a gold medal from the table.
    print("Table without countries with no gold:")
    remove_countries_without_medals(counts, 0, countries)
    
    # Print the new table after editing
    print_table_totals(counts, countries)
    print()

    # Uses dictionaries to save the data and prints it
    medals_dict = {
        "Countries": ["Gold", "Silver", "Bronze"],
        "Canada": [0, 3, 0],
        "Italy": [0, 0, 1],
        "Germany": [0, 0, 1],
        "Japan": [1, 0, 0],
        "Russia": [3, 1, 1],
        "South Korea": [0, 1, 0],
        "United States": [1, 0, 1]
    }

    print("Medals Using Dictionaries:")
    
    for key in medals_dict:
        print("%-10s %s" % (key, medals_dict[key]))
        # print("%-15s" % medals_dict[key], end="")


# Prints the given nested lists and displays only the medals
def print_table(table):
    print("      Gold  Silver  Bronze")
    
    for table_column in range(len(table)):
        for table_row in range(len(table[0])):
            print("%8d" % table[table_column][table_row], end="")
        print()


# Counts all medals by adding all elements one by one
def count_all_medals(table):
    medals = 0
    for i in range(len(table)):
        for j in range(len(table[0])):
            medals = medals + table[i][j]
    return medals


# Counts all medals in the given column, 0 for gold, 1 for silver and 2 for bronze
def count_medals_by_column(table, column):
    total = 0
    for i in range(len(table)):
        total = total + table[i][column]
    return total


# Prints the countries and medals all together in a readable table
def print_table_totals(counts, countries):
    print("        Country      Gold   Silver  Bronze  Medals")

    for i in range(len(countries)):
        print("%15s" % countries[i], end="")

        total = 0
        for j in range(len(counts[0])):
            # print(f"length is {len(counts[0])}")
            print("%8d" % counts[i][j], end="")
            total = total + counts[i][j]
        
        print("%8d" % total)

    gold_medals = count_medals_by_column(counts, 0)
    silver_medals = count_medals_by_column(counts, 1)
    bronze_medals = count_medals_by_column(counts, 2)
    all_medals = count_all_medals(counts)
    print(f"   Total Medals       {gold_medals}       {silver_medals}       {bronze_medals}       {all_medals}")


# Removes the countries without medals in the given table
# 0 for gold, 1 for silver and 2 for bronze
def remove_countries_without_medals(table, column, countries):
    i = 0
    while i < len(table):
        element = table[i][column]
        if element == 0:
            table.pop(i)
            countries.pop(i)
        else:
            i = i + 1


# Start the program   
main()


## Output 1
# Table created for the medals:
#       Gold  Silver  Bronze
#        0       3       0
#        0       0       1
#        0       0       1
#        1       0       0
#        3       1       1
#        0       1       0
#        1       0       1

# The total number of medals is 14
# The total number of gold medals is 5
# The total number of silver medals is 5
# The total number of bronze medals is 4

# Full Table with countries and totals:
#         Country      Gold   Silver  Bronze  Medals
#          Canada       0       3       0       3
#           Italy       0       0       1       1
#         Germany       0       0       1       1
#           Japan       1       0       0       1
#          Russia       3       1       1       5
#     South Korea       0       1       0       1
#   United States       1       0       1       2
#    Total Medals       5       5       4       14

# Table without countries with no gold:
#         Country      Gold   Silver  Bronze  Medals
#           Japan       1       0       0       1
#          Russia       3       1       1       5
#   United States       1       0       1       2
#    Total Medals       5       1       2       8

# Medals Using Dictionaries:
# Countries  ['Gold', 'Silver', 'Bronze']
# Canada     [0, 3, 0]
# Italy      [0, 0, 1]
# Germany    [0, 0, 1]
# Japan      [1, 0, 0]
# Russia     [3, 1, 1]
# South Korea [0, 1, 0]
# United States [1, 0, 1]