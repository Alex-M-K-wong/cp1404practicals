class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language is dynamically typed."""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        return f"{self.name}, {self.typing} typing, Reflection = {self.reflection}, First appeared in {self.year}"


