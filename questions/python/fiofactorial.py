from itertools import combinations

num = int(input())

#1 + 1 + 2 + 3 + 5 + 8
#a(1)==2
#a(2)==3
#a(3)==8
#a(4)==27
#a(5)==125
#a(6)==728
#a(7)==5053
#a(8)==40341
#a(9)==362914
#a(10)==3628855
#a(13)==6227021033

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 


numbers = []
i = 0
n = 0
while n < num:
    #print(f'a({i})=={Fibonacci(i) + factorial(i)}')
    n = Fibonacci(i) + factorial(i)
    numbers.append(n)
    i += 1

#print(numbers)


sums = []
No = False
for i in range(2, len(numbers)+1):
    for com in combinations(numbers, i):
        #print(com)
        #sums.append(sum(com))
        if num == sum(com):
            print(len(com))
            No = True
            
if not No:
    print('NO')




