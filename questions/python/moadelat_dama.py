import numpy as np

a = eval(input())
b = eval(input())


try:
    ans = np.linalg.solve(a, b)
    answer = np.round(ans, 2)
    if (answer >= 0).all() and answer[0] + answer[1] < 100 and answer[2] > 20 and answer[3] > 10:
        print('javab sahih ast')
        print(f'{answer[0]}    {answer[1]}    {answer[2]}    {answer[3]}    bishtarin( T{np.where(answer == answer.max())[0][0]+1}= {answer.max()}) va kamtarin( T{np.where(answer == answer.min())[0][0]+1}= {answer.min()})')
    else:
        print('javab sahih nemibashad')
        
except np.linalg.LinAlgError as e:
    print('javab nadarad')