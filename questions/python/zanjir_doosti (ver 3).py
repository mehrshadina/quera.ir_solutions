n = int(input())
p = {}

def p1(r):
    if r[0] not in p:
        p[r[0]] = [r[1]]
    else:
        p[r[0]].append(r[1])

def p2(r):
    if r[1] not in p:  
        p[r[1]] = [r[0]]
    else:
        p[r[1]].append(r[0])

for number in range(n):
    r = input().split()
    p1(r)
    p2(r)
    
s = input()
pf = p[s]

ff = sorted(list(set([friend for friends in pf for friend in p[friends] if friend != s])))

print(f'Friends of friends of {s}:', ff)
