class Student:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    def bmi(self):
        return self.weight / ((self.height / 100) ** 2)

class Classroom:
    def __init__(self, students):
        self.students = students

    def average_bmi(self):
        return round(sum(map(lambda student: student.bmi(), self.students)) / len(self.students), 1)

    def average_weight(self):
        return round(sum(map(lambda student: student.weight, self.students)) / len(self.students), 1)

class HealthComparison:
    @staticmethod
    def compare(class_a, class_b):
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

students_a = [Student(h, w) for h, w in zip(heights_a, weights_a)]
students_b = [Student(h, w) for h, w in zip(heights_b, weights_b)]

class_a = Classroom(students_a)
class_b = Classroom(students_b)

result = HealthComparison.compare(class_a, class_b)
print(class_a.average_bmi())
print(class_b.average_bmi())
print(result)
