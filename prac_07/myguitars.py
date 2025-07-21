from guitar import Guitar
import csv

def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []
    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    # File format is like: Name,Year,Cost
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Construct a Guitar object using the elements
        # year should be an int
        guitar = Guitar(parts[0], int(parts[1]),float(parts[2]))
        # Add the guitars we've just constructed to the list
        guitars.append(guitar)

    # Close the file as soon as we've finished reading it
    in_file.close()
    #sort the list by year
    guitars.sort()
    # Loop through and display all languages (using their str method)
    for guitar in guitars:
        print(guitar)
    add_new_guitars(guitars)
    guitars.sort()
    save_guitars(guitars)

def add_new_guitars(guitars):
    """Prompt user to add new guitars."""
    print("\nEnter new guitars:")
    name = input("Name: ")
    while name!="":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        name = input("Name: ")

def save_guitars(guitars):
    """Save the list of guitars back to the CSV file."""
    out_file = open('guitars.csv', 'w')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()

"""name = input("What is your name?")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()"""
main()