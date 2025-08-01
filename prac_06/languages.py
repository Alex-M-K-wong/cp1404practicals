"""
languages.py
Estimate: 20 minutes
Actual:   32 minutes
"""
from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

ProgrammingLanguage = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in ProgrammingLanguage:
    if language.is_dynamic():
        print(language.name)