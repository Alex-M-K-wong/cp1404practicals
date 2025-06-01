def main():
    menu = (
        "Menu:\n"
        "(G)et a valid score (must be 0-100 inclusive)\n"
        "(P)rint result\n"
        "(S)how stars\n"
        "(Q)uit"
    )

    choice = input(menu + "\n>>> ").upper()
    score_value = 0
    while choice != "Q":
        if choice == "G":
            score_value = get_valid_score()
        elif choice == "P":
            category_of_result = determine_result(score_value)
            print(category_of_result)
        elif choice == "S":
            print(Show_stars(score_value))
        else:
            print("Invalid choice")
        choice = input(menu + "\n>>> ").upper()

    print("bye")


def Show_stars(score_value):
    return "*" * int(score_value)


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100 inclusive."""
    score_value = float(input("Enter score (0-100): "))
    while score_value < 0 or score_value > 100:
        print("Invalid score. Must be between 0 and 100.")
        score_value = float(input("Enter score (0-100): "))
    return score_value

def determine_result(score):
    """Determine the result category for a given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()