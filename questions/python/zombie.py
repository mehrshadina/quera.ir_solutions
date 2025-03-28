m1, m2 = list(map(int, input().split()))
m3, m4 = list(map(int, input().split()))

fasele = ((m1 - m3) ** 2 + (m2 - m4) ** 2) ** 0.5

print(f'your distance is : {fasele:.2f}')

if fasele == 0:
    print('You are Dead!')
elif fasele < 10:
    print('Run!')
else:
    print('You are safe!')
