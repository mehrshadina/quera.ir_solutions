n = int(input())
pri = list(map(int, input().split()))
m = len(pri)
andaze = int(input())
tarkibat = []
lr = 1

def tarkib1():
    global lr
    pervieous = 0
    for i in range(2, n + 1):
        pervieous, lr = lr, pervieous + lr

def tarkib(start=0, cc=[]):

    if len(cc) == andaze:

        tarkibat.append(cc[:])

        return None
    
    for i in range(
        start, m
        ):
        cc.append(
            pri[i]
            )

        tarkib(i + 1, cc)
        cc.pop()

tarkib1()
tarkib(0)

def count_ways(subset, lr1, tem):
    if lr1 < 0:
        return 0
    
    if lr1 == 0:
        return 1
    
    if lr1 in tem:
        return tem[lr1]


    total_ways = 0
    for p in subset:
        total_ways += count_ways(subset, lr1 - p, tem)

    tem[lr1] = total_ways
    return total_ways

def olgo():
    had_aksar = 0
    #print(tarkibat)
    for sub in tarkibat:
        w2 = count_ways(sub, lr, {})
        #print(w2)
        if w2 > had_aksar:
            had_aksar = w2

    if had_aksar <= 0:
        print("can't reach to this number!")
    else:
        print(had_aksar)

olgo()