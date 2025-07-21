import datetime
class Project:
    """Class to represent a project with name, start date, priority, cost estimate, and percent complete."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = start_date  # datetime.date object
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.percent_complete = percent_complete

    def __str__(self):
        date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.percent_complete}%")

    def is_complete(self):
        """Return True if project is completed."""
        return self.percent_complete >= 100

    def __lt__(self, other):
        """Sort by priority."""
        return self.priority < other.priority