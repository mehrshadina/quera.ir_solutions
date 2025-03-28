n = int(input())

matrix = [input().split() for _ in range(n)]
indexed_matrix = [(line, i) for i, line in enumerate(matrix)]

indexed_matrix.sort(key=lambda x: (len(x[0]), list(map(int, x[0]))))

line_to_letter = {}
current_letter = "A"
for line, original_index in indexed_matrix:
    line_tuple = tuple(line)
    if line_tuple not in line_to_letter:
        line_to_letter[line_tuple] = current_letter
        current_letter = chr(ord(current_letter) + 1)

result = [''] * n
for line, original_index in indexed_matrix:
    line_tuple = tuple(line)
    result[original_index] = line_to_letter[line_tuple]

print(''.join(result))
