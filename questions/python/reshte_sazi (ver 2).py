n = int(input())
matrix = [input().split() for _ in range(n)]
sorted_matrix = sorted(
    matrix, 
    key=lambda x: (
        len(x), 
        list(
            map(int, x)
            )
            )
            )
current_letter = "A"
lastRow = sorted_matrix[0]

for line in sorted_matrix:

    if line != lastRow:

        current_letter = chr(
            ord(current_letter) + 1
            )

    matrix[
        matrix.index(line)
        ] = current_letter

    lastRow = line

word = ''

for m in matrix:

    word += m

print(word)