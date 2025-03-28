pupulation = {}
n = int(input())

for _ in range(n):
    relation = input().split()
    person1, person2 = relation[0], relation[1]

    if person1 not in pupulation:
        pupulation[person1] = [person2]
    else:
        pupulation[person1].append(person2)

    if person2 not in pupulation:
        pupulation[person2] = [person1]
    else:
        pupulation[person2].append(person1)

# Input the person to search for
personality = input().strip()

# Get the friends of the searched person
person_friends = pupulation.get(personality, [])
# Find friends of friends, excluding the original person
friends_of_friends = [
    friend
    for friends in person_friends
    for friend in pupulation.get(friends, [])
    if friend != personality
]

# Remove duplicates and sort the list
friends_of_friends = sorted(set(friends_of_friends))

# Output the result
print(f'Friends of friends of {personality}:', friends_of_friends)
