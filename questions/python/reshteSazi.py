def sort_matrix(matrix):
    return sorted(matrix, key=lambda x: (len(x), list(map(int, x))))

def assign_letters(matrix, sorted_matrix):
    letter = "A"
    lastRow = sorted_matrix[0]
    
    for row in sorted_matrix:
        if row != lastRow:
            letter = chr(ord(letter) + 1)
        matrix[matrix.index(row)] = letter
        lastRow = row

    return ''.join(matrix)

def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix

def main():
    n = int(input())
    matrix = read_matrix(n)
    sorted_matrix = sort_matrix(matrix)
    result = assign_letters(matrix, sorted_matrix)
    print(result)

main()
