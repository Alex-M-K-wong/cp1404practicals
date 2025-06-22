"""
Word Occurrences
Estimate: 20 minutes
Actual:   32 minutes
"""

def main():
    with open("wimbledon.csv", "r") as file:
        lines = file.readlines()

    lines = lines[1:]

    champion_wins = {}
    countries = set()

    for line in lines:
        parts = line.strip().split(",")
        country = parts[1]    # Winner's country
        name = parts[2]       # Winner's name

        # Count the wins
        if name in champion_wins:
            champion_wins[name] += 1
        else:
            champion_wins[name] = 1

        # Add country to the set
        countries.add(country)

    # Print the results
    print("Wimbledon Champions:")
    for name in sorted(champion_wins):
        print(f"{name} {champion_wins[name]}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()