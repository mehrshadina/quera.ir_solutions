n = int(input())
fib = [0, 1]
combs = []
hazineh = list(map(int, input().split()))
ss = int(input())

for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])
lnumber = fib[n]

n = len(hazineh)

def count_ways(subset, lnumber, just_a_set):
    if lnumber == 0:
        return 1
    
    elif lnumber < 0:
        return 0
    
    elif lnumber in just_a_set:
        return just_a_set[lnumber]

    tw = 0
    for price2 in subset:
        #print(delta)
        tw += count_ways(subset, lnumber - price2, just_a_set)

    just_a_set[lnumber] = tw
    return tw

def function(start, combin=[]):
    """
    This function recursively generates all possible combs of hazineh from the 'hazineh' list,
    starting from a given index and adding elements to the 'combin' list until the length of 'combin'
    equals the specified length 'ss'. Each valid combination is added to the global 'combs' list.
    """
    if len(combin) == ss:
        combs.append(combin[:])
        return
    
    for i in range(start, n):
        combin.append(hazineh[i])

        function(
            i + 1, combin
            )

        combin.pop()

function(0)
tootal = 0

def calculate():
    global tootal
    #print(combs)
    for sub in combs:
        ways = count_ways(sub, lnumber, {})
        #print(ways)
        
        if ways > tootal:
            tootal = ways


calculate()

if tootal <= 0:
    print("can't reach to this number!")



if tootal > 0:
    print(tootal)
