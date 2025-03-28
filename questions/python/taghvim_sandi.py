from datetime import datetime

month = int(input())
year = int(input())

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
for day in days:
    print(day, end="\t")
print()

month_days = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month]
start_day = datetime(year, month, 1).weekday()

line = []

for i in range(start_day):
    line.append(" ")

for day in range(1, month_days + 1):
    line.append(str(day))
    if len(line) == 7:
        for value in line:
            print(value, end="\t")
        print()
        line = []

if line:
    for value in line:
        print(value, end="\t")
    print()
