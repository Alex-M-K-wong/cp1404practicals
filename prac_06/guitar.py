CORRECT_YEAR = 2022 #example year
AGE_LIMIT =50

class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
      return f"{self.name} ({self.year} : ${self.cost})"

    def get_age(self):
        age = CORRECT_YEAR - self.year
        return age


    def is_vintage(self):
        age = self.get_age()
        if age >= AGE_LIMIT:
            return True
        else:
            return False