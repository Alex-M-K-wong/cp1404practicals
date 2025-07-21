"""
Project Management Program
Time Estimate: ~2 hours
"""

from project import Project
import datetime

FILENAME = "projects.txt"


def main():
    """Main menu for project management."""
    projects = load_projects(FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = ("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n"
            "- (F)ilter projects by date\n- (A)dd new project\n"
            "- (U)pdate project\n- (Q)uit")

    print(menu)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'l':
            filename = input("Filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            return
        elif choice == 'a':
            return
        elif choice == 'u':
            return
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>> ").lower()

    save = input(f"Would you like to save to {FILENAME}? ").lower()
    if save == 'y' or save == 'yes':
        save_projects(FILENAME, projects)

    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.datetime.strptime(parts[1], "%d/%m/%Y").date()
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            percent_complete = int(parts[4])
            projects.append(Project(name, start_date, priority, cost_estimate, percent_complete))
    return projects


def save_projects(filename, projects):
    """Save projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            date_string = project.start_date.strftime("%d/%m/%Y")
            file.write(f"{project.name}\t{date_string}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.percent_complete}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]
    incomplete.sort()
    complete.sort()
    print("Incomplete projects: ")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects: ")
    for project in complete:
        print(f"  {project}")


main()