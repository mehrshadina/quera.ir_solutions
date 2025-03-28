def ezafe_kardan_relation(mardom, shakhs1, shakhs2):
    if shakhs1 not in mardom:
        mardom[shakhs1] = [shakhs2]
    else:
        mardom[shakhs1].append(shakhs2)

    if shakhs2 not in mardom:
        mardom[shakhs2] = [shakhs1]
    else:
        mardom[shakhs2].append(shakhs1)

def peyda_kardan_dostan_dostan(mardom, donbal_shakhs):
    dostan_shakhs = mardom[donbal_shakhs]
    dostan_dostan = [dost for dostan in dostan_shakhs for dost in mardom[dostan] if dost != donbal_shakhs]
    dostan_dostan = sorted(list(set(dostan_dostan)))
    return dostan_dostan

def dost_function():
    pass

tedad = int(input())
mardom = {}

for _ in range(tedad):
    relation = input().split()
    ezafe_kardan_relation(mardom, relation[0], relation[1])

donbal_shakhs = input().strip()
dostan_dostan = peyda_kardan_dostan_dostan(mardom, donbal_shakhs)

for dostan in mardom[donbal_shakhs]:
    for dost in mardom[dostan]:
        dost

print(f'Friends of friends of {donbal_shakhs}:', dostan_dostan)

def payda_konande():
    return None
