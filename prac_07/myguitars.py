from guitar import Guitar

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



main()