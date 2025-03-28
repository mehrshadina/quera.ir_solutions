n = int(input())
people = {}

for _ in range(n):
    realation = input().split()

    for i, j in [(realation[0], realation[1]), (realation[1], realation[0])]:
        if i not in people:
            people[i] = [j]
        else:
            people[i].append(j)
    
find = input().strip()
person_friends = people.get(find, [])

friends = set()

for friend in person_friends:
    for foaf in people.get(friend, []):  # 'foaf' stands for 'friend of a friend'
        if foaf != find and foaf not in person_friends:
            friends.add(foaf)

friends = sorted(friends)

print(f'Friends of friends of {find}:', friends)
