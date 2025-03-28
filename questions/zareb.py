start, end = map(int, input().split())

result = 1
for i in range (start+1, end):
    result = result * i

print(result)