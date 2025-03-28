def solve_partial_pivoting(A, b):
    n = len(A)

    for i in range(n):
        max_i = i

        for j in range(i+1, n):
            if not (abs(A[j][i]) <= abs(A[max_i][i])):
                max_i = j

        A[i], A[max_i] = A[max_i], A[i]

        b[i], b[max_i] = b[max_i], b[i]

        for j in range(i+1, n):
            fac = A[j][i] / A[i][i]

            for k in range(i, n):
                A[j][k] -= fac * A[i][k]

            b[j] -= fac * b[i]

    x = [0] * n
    for i in range(n-1, -1, -1):

        sum = b[i]
        
        for j in range(i+1, n):
            sum -= A[i][j] * x[j]
        x[i] = sum / A[i][i]

    return x

def main ():
    A = []
    b = []

    formula = list(
        map(
            float, 
            input().split()
            )
        )
    A.append(formula[:-1])
    b.append(formula[-1])

    n = len(formula) -1

    for _ in range(len(formula)-2):
        formula = list(
            map(float,
                input().split()
                )
            )
        A.append(formula[:-1])
        b.append(formula[-1])

    x = solve_partial_pivoting(A, b)

    for i in range(n):
        print(f"x{i+1} = {x[i]:.3f}")

main()