n = eval(input())
numbers_array = []

for _ in range(n):
    numbers_array.append(input().split())

sorted_numbers_array = sorted(
    numbers_array, 
    key=lambda x: (
        len(x), 
        list(map(int, x))
        )
        )

current = "A"
ll = sorted_numbers_array[0]

for line in sorted_numbers_array:
    
    if line != ll:
        current = chr(ord(current) + 1)

    numbers_array[numbers_array.index(line)] = current
    ll = line

text = ''.join(numbers_array)
print(
    text
    )