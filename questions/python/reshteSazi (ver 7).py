n = int(input())

matrix = [input().split() for _ in range(n)]
sorted_matrix = sorted(enumerate(matrix), key=lambda x: (len(x[1]), list(map(int, x[1]))))

letters = [""] * n
current_letter = "A"
last_line = sorted_matrix[0][1]

for index, line in sorted_matrix:
    if line != last_line:
        current_letter = chr(ord(current_letter) + 1)
    letters[index] = current_letter
    last_line = line

result = ''.join(letters)
print(result)
