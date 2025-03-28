n,k  = list(map(int, input().split()))

count = 1
while n > k:
    k = k + k
    count +=1

print(count)
