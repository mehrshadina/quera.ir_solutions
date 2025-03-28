rows, cols, a = map(int, input().split())

board = []
for _ in range(rows):
    row = list(map(int, input().split()))
    board.append(row)

#print(board)

def matrix_diagnolans(matrix):
    diagonals = []

    for j in range(cols):
        diagonals.append([matrix[i][j] for i in range(rows)])

    for i in range(rows):
        diagonals.append(matrix[i])

    # Main diagonal and diagonals above it
    # Traverse diagonals above the main diagonal
    for i in range(cols):
        diagonal = [matrix[j][i + j] for j in range(rows) if 0 <= i + j < cols]
        diagonals.append(diagonal)

    # Traverse diagonals below the main diagonal
    for i in range(1, rows):
        diagonal = [matrix[i + j][j] for j in range(cols) if 0 <= i + j < rows]
        diagonals.append(diagonal)

    # Main reverse diagonal and diagonals above it
    for j in range(cols):
        diagonal = [matrix[i][j - i] for i in range(min(j+1, rows))]
        diagonals.append(diagonal)

    # Diagonals below the main reverse diagonal
    for i in range(1, rows):
        diagonal = [matrix[i + k][cols - k - 1] for k in range(min(rows - i, cols))]
        diagonals.append(diagonal)

    return diagonals

scores = [0] * a
diagnosal = matrix_diagnolans(board)
#print(diagnosal)
for row in diagnosal:
    last_num = 0
    count = 1
    #print(row)
    for num in row:
        #print(num, count)
        if num == last_num:
            count += 1
        else:
            
            last_num = num
            count = 1
        scores[num - 1] = max(count, scores[num - 1])
        #scores[num - 1] = max(count, scores[num - 1])
    #print(scores)

print(*scores)