students = []
n = int(input())

for _ in range(n):
    srudent_information = input().split()
    
    all_grades = list(map(float, srudent_information[3:]))
    #print(all_grades)
    grades = all_grades[0::2]
    weights = all_grades[1::2]
    #print(weights)
    
    weighted_sum = 0
    for g, u in zip(grades, weights):
        weighted_sum += g * u
    avarage = round(weighted_sum / sum(weights), 2)

    student = (
        srudent_information[0],
        "%s %s"%(srudent_information[1], srudent_information[2]),
        sum(weights),
        avarage,
        )
    #print(student)
    students.append(student)
    

students.sort(key=lambda x: (-x[3], x[0]))


with open('result.csv', 'w') as csvfile:
    first_line = 'studentNumber, FullName, Num_Of_Units, Avg\n'
    csvfile.write(first_line)
    
    for student in students:
        csvfile.write(
            f'{student[0]}, {student[1]}, {student[2]}, {student[3]}\n'
        )


