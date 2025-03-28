class Student:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / ((self.height / 100) ** 2)

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def average_bmi(self):
        total_bmi = sum(student.calculate_bmi() for student in self.students)
        return round(total_bmi / len(self.students), 1)

    def average_weight(self):
        total_weight = sum(student.weight for student in self.students)
        return round(total_weight / len(self.students), 1)

def compare_classes(class_a, class_b):
    avg_bmi_a = class_a.average_bmi()
    avg_bmi_b = class_b.average_bmi()
    if avg_bmi_a < avg_bmi_b:
        return "A"
    elif avg_bmi_b < avg_bmi_a:
        return "B"
    else:
        avg_weight_a = class_a.average_weight()
        avg_weight_b = class_b.average_weight()
        if avg_weight_a < avg_weight_b:
            return "A"
        elif avg_weight_b < avg_weight_a:
            return "B"
        else:
            return "Same"

num_students_a = int(input())
heights_a = list(map(int, input().split()))
weights_a = list(map(int, input().split()))

num_students_b = int(input())
heights_b = list(map(int, input().split()))
weights_b = list(map(int, input().split()))

class_a = Classroom()
class_b = Classroom()

for height, weight in zip(heights_a, weights_a):
    class_a.add_student(Student(height, weight))

for height, weight in zip(heights_b, weights_b):
    class_b.add_student(Student(height, weight))

result = compare_classes(class_a, class_b)
print(class_a.average_bmi())
print(class_b.average_bmi())
print(result)
