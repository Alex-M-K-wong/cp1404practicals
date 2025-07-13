"""
Estimated time : 30 minutes
Actual time : 20 minutes
"""

from prac_06.guitar import Guitar

Guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
Guitar2 = Guitar("Another Guitar", 2013, 0)


print(f"{Guitar1.name} get_age() - Expected 100. Got {Guitar1.get_age()}")
print(f"{Guitar2.name} get_age() - Expected 9. Got {Guitar2.get_age()}")


print(f"{Guitar1.name} is_vintage() - Expected True. Got {Guitar1.is_vintage()}")
print(f"{Guitar2.name} is_vintage() - Expected False. Got {Guitar2.is_vintage()}")
