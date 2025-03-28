total_activities = int(input())
activities = [input() for i in range(7)]

days = ["Monday",
         "Tuesday", 
         "Wednesday", 
         "Thursday", 
         "Friday", 
         "Saturday", 
         "Sunday"
         ]
activity_map = {day: [] for day in days}

for activity in activities:
    day, _, *acts = activity.split()
    activity_map[day] = list(map(int, acts))

#print(activity_map)

#min_distance = float('inf')

for i in range(7):
    for j in range(i + 1, 7):
        #print(activity_map[days[i]], '/', activity_map[days[j]], end=' ')
        common_activities = set(activity_map[days[i]]) & set(activity_map[days[j]])
        if common_activities:
            distance = abs(j - i)
            #min_distance = min(min_distance, distance)
            #print(set(activity_map[days[i]]) - set(activity_map[days[j]]), ' ', set(activity_map[days[j]]) - set(activity_map[days[i]]))
            if set(activity_map[days[i]]) - set(activity_map[days[j]]) and set(activity_map[days[j]]) - set(activity_map[days[i]]):
                print(distance) if distance < 4 else print(7 - distance)

print(-1)