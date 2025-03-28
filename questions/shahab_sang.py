meteorites = list(map(int, input().split()))
meteorites2 = []

#print(meteorites)
i = 1
step = 1
while i < len(meteorites):
    if meteorites[i-1] > 0 and meteorites[i] < 0:
        remaning = meteorites[i-1] + meteorites[i]
        if meteorites[i-1] ==  -meteorites[i]:
            print(f'step {step}: meteorite with index {i-1} and {i} with size {meteorites[i-1]} exploded')
            meteorites = meteorites[:i-1] + meteorites[i+1:]
            i -= 1
        else:
            if meteorites[i-1] + meteorites[i] > 0:
                print(f'step {step}: meteorite with index {i} with size {meteorites[i]} exploded')
                meteorites = meteorites[:i-1] + [remaning] + meteorites[i+1:]
            else:
                print(f'step {step}: meteorite with index {i-1} with size {meteorites[i-1]} exploded')
                i -= 1
                meteorites = meteorites[:i] + [remaning] + meteorites[i+2:]
        print('new orbit:', meteorites)
        step += 1
        
    else:
        i += 1
        #print('\n')
        #print(i, end=' ')


print('final orbit:', meteorites)