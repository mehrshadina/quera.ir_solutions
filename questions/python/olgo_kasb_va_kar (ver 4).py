n = int(input())
gheymatha = list(map(int, input().split()))
size_kombinasion = int(input())
a = 0 
b = 1
for i in range(2, n + 1):
    a, b = b, a+b
akhare_adad = b
n = len(gheymatha)
kombinasion_ha = []

def donbal_konandeh(start, current_combination=[]):
    if len(current_combination) == size_kombinasion:
        kombinasion_ha.append(current_combination[:])
        return
    
    for i in range(start, n):
        current_combination.append(gheymatha[i])
        donbal_konandeh(i + 1, current_combination)
        current_combination.pop()

def hesab_kon(subset, hadaf, temp_set):
    if hadaf == 0:
        return 1
    elif hadaf < 0:
        return 0
    
    if hadaf in temp_set:
        return temp_set[hadaf]

    total_ways = 0
    for gheymat in subset:
        delta = hadaf - gheymat
        total_ways += hesab_kon(subset, delta, temp_set)

    temp_set[hadaf] = total_ways
    return total_ways

def peyda_kardane_max_ways():
    max_ways = 0
    for sub in kombinasion_ha:
        temp_set = {}
        ways = hesab_kon(sub, akhare_adad, temp_set)
        if ways > max_ways:
            max_ways = ways
    

    if max_ways > 0:
        print(max_ways)
    else:
        print("can't reach to this number!")


donbal_konandeh(0)
peyda_kardane_max_ways()

