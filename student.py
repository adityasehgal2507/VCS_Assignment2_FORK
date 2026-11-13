from dataclasses import dataclass

@dataclass
class Student:
    name: str
    section: str


print("Student Management System")

def print_name(name):
    print("Student name:", name)

def print_section(section):
    print("Student section:", section)

s = Student("Inu Chetry", "3B")
print_name(s.name)
print_section(s.section)
