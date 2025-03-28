def distance(lines, total_lines):
    week_days = [ "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    map = {day: [] for day in week_days}

    for act in lines:
        day, _, *acts = act.split()
        map[day] = []
        for a in acts:
            map[day].append(int(a))

    for i in range(7):
        for j in range(i + 1, 7):
            common_activities = set(map[week_days[i]]) & set(map[week_days[j]])
            if common_activities:
                dist = abs(j - i)
                if set(map[week_days[i]]) - set(map[week_days[j]]):
                    if set(map[week_days[j]]) - set(map[week_days[i]]):
                        return dist if dist < 4 else 7 - dist
    return -1

def main():
    total_lines = int(input())
    lines = []
    for _ in range(7):
        lines.append(input())

    print(distance(lines, total_lines))

main()