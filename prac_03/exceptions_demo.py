"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Ans: when numerator and denominator are not valid numbers!
2. When will a ZeroDivisionError occur?
Ans: when the denominator is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Ans: I try.No no no, I can.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("denominator can not be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")