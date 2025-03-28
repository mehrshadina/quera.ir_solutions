n = int(input())
p = {}

def a():
    for _ in range(n):
        realation = input().split()

        if realation[0] not in p:
            p[realation[0]] = [realation[1]]
        else:
            p[realation[0]].append(realation[1])

        if realation[1] not in p:  
            p[realation[1]] = [realation[0]]
        else:
            p[realation[1]].append(realation[0])

def find_friens(person_friends):
    return [friend for friends in person_friends for friend in p[friends] if friend != query]

a()
query = input().strip()
friends = find_friens(p[query])
print(f'Friends of friends of {query}:', friends)
