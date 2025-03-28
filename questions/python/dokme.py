m, n  = list(map(int, input().split()))

count = 0
while n < m:
    n = n * 2
    count +=1
    
while n > m:
    n -= 1
    count += 1

print(count)