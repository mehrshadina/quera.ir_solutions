from collections import defaultdict

n = int(input())
people = defaultdict(list)

for _ in range(n):
    relation = input().split()
    person1, person2 = relation[0], relation[1]

    people[person1].append(person2)
    people[person2].append(person1)
    
search_for = input().strip()
person_friends = people.get(search_for, [])

friends_of_friends = []

for friend in person_friends:
    if friend in people:
        for foaf in people[friend]:
            if foaf != search_for and foaf not in person_friends and foaf not in friends_of_friends:
                friends_of_friends.append(foaf)

friends_of_friends.sort()

print(f'Friends of friends of {search_for}:', friends_of_friends)