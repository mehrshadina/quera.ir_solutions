def pad_matrix(matrix: list[list[int]]):
    new_matrix = []
    n = len(matrix[0])
    zeroes = [0 for i in range(n+2)]
    
    new_matrix.append(zeroes)

    for row in matrix:
        new_matrix.append([0] + row + [0])

    new_matrix.append(zeroes)

    return new_matrix
    

def inner_product_3x3(matrix1: list[list[int]], matrix2: list[list[int]]):
    answer = 0
    for i in range(3):
        for j in range(3):
            answer += matrix1[i][j] * matrix2[i][j]

    return(answer)


def convolve_3x3_kernel(matrix: list[list[int]], kernel: list[list[int]]):
    padded_matrix = pad_matrix(matrix)
    rows, cols = len(matrix), len(matrix[0])
    output = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            value = 0
            for ki in range(3):
                for kj in range(3):
                    value += padded_matrix[i + ki][j + kj] * kernel[ki][kj]
            output[i][j] = value
    
    return output
