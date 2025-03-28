n = 0
prices = []
subSize = 0
combinations = []
maximumWays = 0

def count_ways(subset, end, sett):
    if end == 0:
        return 1
    elif end < 0:
        return 0
    
    if end in sett:
        return sett[end]

    total_ways = 0
    for price in subset:
        delta = end - price
        
        total_ways += count_ways(subset, delta, sett)

    sett[end] = total_ways
    return total_ways

def tracker(sendt, current_combination=[]):
    if len(current_combination) == subSize:
        combinations.append(current_combination[:])
        return
    
    for i in range(sendt, n):
        current_combination.append(prices[i])
        tracker(i + 1, current_combination)
        current_combination.pop()
        

def main():
    global n, prices, subSize, combinations, maximumWays

    n = int(input())
    prices = list(map(int, input().split()))
    subSize = int(input())

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i-1] + fib[i-2])
    last_number = fib[n]

    n = len(prices)
    tracker(0)
    
    for sub in combinations:
        sett = {}
        
        ways = count_ways(sub, last_number, sett)
        
        if ways > maximumWays:
            maximumWays = ways

    if maximumWays > 0:
        print(maximumWays)
    else:
        print("can't reach to this number!")
        
main()