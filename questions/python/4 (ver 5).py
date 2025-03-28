n = int(input())

matrix = [input().split() for _ in range(n)]

sorted_matrix = sorted(matrix, key=lambda x: (len(x), list(map(int, x))))

line_to_letter = {}
current_letter = "A"

for line in sorted_matrix:
    line_tuple = tuple(line)
    if line_tuple not in line_to_letter:
        line_to_letter[line_tuple] = current_letter
        current_letter = chr(ord(current_letter) + 1)

result = ''.join(line_to_letter[tuple(line)] for line in matrix)

print(result)
