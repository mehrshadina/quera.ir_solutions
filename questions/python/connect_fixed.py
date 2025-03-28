m, n, a = map(int, input().split())
lines = []
matrix = []
result = [0] * a

for i in range(m):
    row = []
    for num in input().split():
        row.append(int(num))
    matrix.append(row)

for i in range(m):
    lines.append(matrix[i])

for j in range(n):
    array = []
    for i in range(m):
        array.append(matrix[i][j])
    lines.append(array)

for i in range(1, m):
    array = []
    for j in range(n):
        if 0 <= i + j < m:
            array.append(matrix[i + j][j])
    lines.append(array)

for i in range(n):
    array = []
    for j in range(m):
        if 0 <= i + j < n:
            array.append(matrix[j][i + j])
    lines.append(array)

for j in range(n):
    array = []
    for i in range(min(j+1, m)):
        array.append(matrix[i][j - i])
    lines.append(array)

for i in range(1, m):
    array = []
    for k in range(min(m - i, n)):
        array.append(matrix[i + k][n - k - 1])
    lines.append(array)

for line in lines:
    last = 0
    count = 1
    for number in line:
        if number == last:
            count += 1
        else:
            last = number
            count = 1
        result[number - 1] = max(count, result[number - 1])

for i in result:
    print(i, end=' ')
