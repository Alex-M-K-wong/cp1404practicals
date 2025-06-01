"""
get items number
total price = 0
for i in range items number
    get price of item
    total price += price of item
if total price >100
    total price *=0.9
    print total price
"""
number_of_items = int(input("Number of items:"))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

total_price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item:"))
    total_price+= price_of_item
if total_price >100:
    total_price *= 0.9
    print(f"Total price for {number_of_items} items is ${total_price:.2f}")
