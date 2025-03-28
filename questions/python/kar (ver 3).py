n = int(input())
prices = list(map(int, input().split()))
size = int(input())
all_combinaations = []

def mixer(
        start, 
        current=[]
        ):
    if len(current) == size:
        all_combinaations.append(current[:])

        return
    
    for i in range(start, len(prices)):
        current.append(prices[i])

        mixer(i + 1, current)

        current.pop()

def all_ways(
        subsetset, 
        thing, 
        temp_set
        ):
    
    if thing < 0:
        return 0
    
    if thing == 0:
        return 1
    
    if thing in temp_set:
        return temp_set[thing]

    total_ways = 0
    for price in subsetset:
        delta = thing - price
        total_ways += all_ways(subsetset, delta, temp_set)

    temp_set[thing] = total_ways
    return total_ways


mixer(0)
most_logest_way = 0
a, b = 0, 1

for i in range(2, n + 1):
    c = a + b
    a,b = b, c
last_number = b

for subset in all_combinaations:
    temp_set = {}
    ways = all_ways(subset, last_number, temp_set)
    
    if ways > most_logest_way:
        most_logest_way = ways

if most_logest_way <= 0:
    print("can't reach to this number!")
else:
    print(most_logest_way)
