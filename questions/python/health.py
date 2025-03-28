from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    height: int
    weight: int

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

@dataclass
class Classroom:
    students: List[Student]

    def average_bmi(self):
        return round(sum(student.bmi() for student in self.students) / len(self.students), 1)

    def average_weight(self):
        return round(sum(student.weight for student in self.students) / len(self.students), 1)

def compare_classes(class_a, class_b):
    if class_a.average_bmi() < class_b.average_bmi():
        return "A"
    elif class_a.average_bmi() > class_b.average_bmi():
        return "B"
    else:
        if class_a.average_weight() < class_b.average_weight():
            return "A"
        elif class_a.average_weight() > class_b.average_weight():
            return "B"
        else:
            return "Same"

num_students_a = int(input())
heights_a = list(map(int, input().split()))
weights_a = list(map(int, input().split()))

num_students_b = int(input())
heights_b = list(map(int, input().split()))
weights_b = list(map(int, input().split()))

students_a = [Student(h, w) for h, w in zip(heights_a, weights_a)]
students_b = [Student(h, w) for h, w in zip(heights_b, weights_b)]

class_a = Classroom(students_a)
class_b = Classroom(students_b)

result = compare_classes(class_a, class_b)
print(class_a.average_bmi())
print(class_b.average_bmi())
print(result)
