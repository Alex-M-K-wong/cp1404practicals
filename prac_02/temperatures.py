"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
def main():
    MENU = """C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = converting_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = converting_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def converting_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / (9.0 / 5)


def converting_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()