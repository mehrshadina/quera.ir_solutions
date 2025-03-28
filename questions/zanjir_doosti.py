n = int(input())
people = {}

for _ in range(n):
    realation = input().split()

    if realation[0] not in people:
        people[realation[0]] = [realation[1]]
    else:
        people[realation[0]].append(realation[1])


    if realation[1] not in people:  
        people[realation[1]] = [realation[0]]
    else:
        people[realation[1]].append(realation[0])
    
search_for = input().strip()
person_friends = people[search_for]
#print(person_friends)

friends_of_friends = [friend for friends in person_friends for friend in people[friends] if friend != search_for]
friends_of_friends = sorted(list(set(friends_of_friends)))


for friends in person_friends:
    for friend in people[friends]:
        friend

print(f'Friends of friends of {search_for}:', friends_of_friends)
