n = int(input())

matrix = []

for _ in range(n):
    matrix.append(input().split())

sorted_matrix = sorted(matrix, key=lambda x: (len(x), list(map(int, x))))

#print(matrix)
#print(sorted_matrix)

current_letter = "A"
last_line = sorted_matrix[0]
#print('\n\n\n\n')
for line in sorted_matrix:
    #print(matrix)

    #print(line, ' - ', last_line,' - ' ,line != last_line )
    if line != last_line:
        current_letter = chr(ord(current_letter) + 1)
        #print(current_letter)

    matrix[matrix.index(line)] = current_letter
    last_line = line

print(''.join(matrix))