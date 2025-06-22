"""
Word Occurrences
Estimate: 30 minutes
Actual:   40 minutes
"""
def main():
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name_guess = get_name_from_email(email)
        confirmation = input(f"Is your name {name_guess}? (Y/n) ").strip().lower()

        if confirmation not in ('', 'y', 'yes'):
            name = input("Name: ").strip()
        else:
            name = name_guess

        email_to_name[email] = name
        email = input("Email: ").strip()


    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    """Extract a name from the given email."""
    name_part = email.split('@')[0]
    parts = name_part.replace('.', ' ').split()
    return " ".join(parts).title()

main()