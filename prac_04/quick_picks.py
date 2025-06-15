import random



def main():
    quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        line = generate_quick_pick()
        print(*[f"{number:2}" for number in line])

def generate_quick_pick():
    """Generate one quick pick (6 unique numbers)."""
    MIN_NUMBER = 1
    MAX_NUMBER = 45
    NUMBERS_PER_LINE = 6
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)
    quick_pick.sort()
    return quick_pick

main()
