def partial(mA, mb):
    n = len(mA)

    for i in range(n):
        maximum_i = i

        for j in range(i + 1, n):
            if abs(mA[j][i]) > abs(mA[maximum_i][i]):
                maximum_i = j

        c = mA[i]
        mA[i] = mA[maximum_i]
        mA[maximum_i] = c

        d = mb[i]
        mb[i] = mb[maximum_i]
        mb[maximum_i] = d

        for j in range(i+1, n):
            f = mA[j][i]/mA[i][i]
            
            for k in range(i, n):
                mA[j][k] -= f*mA[i][k]
            mb[j] -= f*mb[i]

    allX = [0] * n
    
    for i in range(n-1, -1, -1):
        sum_term = mb[i]
        
        for j in range(i+1, n):
            sum_term -= mA[i][j] * allX[j]
        allX[i] = sum_term / mA[i][i]

    n = len(allX)
    for i in range(n):
        print(f"x{i+1}", 
              "=", 
              f"{allX[i]:.3f}"
        )


matrixA = []
matrixB = []
eq = list(map(float, input().split()))
matrixB.append(eq[-1])
matrixA.append(eq[:-1])

count = 0
while count < len(eq)-2:
    eq = list(map(float, input().split()))
    matrixB.append(eq[-1])
    matrixA.append(eq[:-1])

    count += 1

partial(matrixA, matrixB)



