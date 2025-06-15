import random



def main():
    quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        line = generate_quick_pick()
        print(*[f"{number:2}" for number in line])

def generate_quick_pick():
    """Generate one quick pick (6 unique numbers)."""
    min_number = 1
    max_number = 45
    numbers_per_line = 6
    quick_pick = []
    while len(quick_pick) < numbers_per_line:
        number = random.randint(min_number, max_number)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

main()
