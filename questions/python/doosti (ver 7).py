n = int(input())
people = {}

for _ in range(n):
    relation = input().split()
    person1, person2 = relation[0], relation[1]

    people.setdefault(person1, []).append(person2)
    people.setdefault(person2, []).append(person1)

search_for = input().strip()
person_friends = people.get(search_for, [])

friends_of_friends_dict = {}

for friend in person_friends:
    if friend in people:
        for foaf in people[friend]:
            if foaf != search_for and foaf not in person_friends:
                friends_of_friends_dict[foaf] = True

friends_of_friends = sorted(friends_of_friends_dict.keys())

print(f'Friends of friends of {search_for}:', friends_of_friends)
