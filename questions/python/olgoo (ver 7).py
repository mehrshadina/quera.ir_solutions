n = int(input())
gheymatha = list(map(int, input().split()))
r = int(input())
p = len(gheymatha)

x, y = 0, 1
for i in range(2, n + 1):
    x, y = y, x+y

halatha = []
last_ = y

def count_ways(subset, l, temp_set):
    if l == 0:
        return 1
    
    if l < 0:
        return 0
    
    if l in temp_set:
        return temp_set[l]

    total_ways = 0
    for e in subset:
        tafavot = l - e
        total_ways += count_ways(subset, tafavot, temp_set)

    temp_set[l] = total_ways
    return total_ways

def main():
    mw = 0
    for sub in halatha:
        temp_set = {}
        ways = count_ways(sub, last_, temp_set)
        
        if ways > mw:
            mw = ways

    if mw > 0:
        print(mw)
    else:
        print("can't reach to this number!")

def machine(start=1, moment=[]):
    #print(moment)
    if len(moment) == r:
        halatha.append(moment[:])
        return
    
    for i in range(start, p):

        moment.append(
            gheymatha[i]
            )
        machine(i + 1, moment)

        moment.pop()

machine(0)
main()