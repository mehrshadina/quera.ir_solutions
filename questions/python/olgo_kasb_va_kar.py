n = int(input())
prices = list(map(int, input().split()))
sub_size = int(input())

fib = [0, 1]
for i in range(2, n + 1):
    fib.append(fib[i-1] + fib[i-2])
last_number = fib[n]

n = len(prices)
combinations = []

def tracker(start, current_combination=[]):
    if len(current_combination) == sub_size:
        combinations.append(current_combination[:])
        return
    
    for i in range(start, n):
        current_combination.append(prices[i])
        tracker(i + 1, current_combination)
        current_combination.pop()
        #print(current_combination)

tracker(0)

def count_ways(subset, tar, temp_set):
    if tar == 0:
        return 1
    elif tar < 0:
        return 0
    
    if tar in temp_set:
        return temp_set[tar]

    total_ways = 0
    for price in subset:
        delta = tar - price
        #print(delta)
        total_ways += count_ways(subset, delta, temp_set)

    temp_set[tar] = total_ways
    return total_ways

maximum_ways = 0
for sub in combinations:
    temp_set = {}
    #print(sub)
    ways = count_ways(sub, last_number, temp_set)
    
    if ways > maximum_ways:
        maximum_ways = ways

if maximum_ways > 0:
    print(maximum_ways)
else:
    print("can't reach to this number!")
