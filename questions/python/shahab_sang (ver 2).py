shahab = list(map(int, input().split()))
count = 1
i = 1

def check():
    global shahab, i
    if shahab[i-1] + shahab[i] > 0:
        print(f'step {count}: meteorite with index {i} with size {shahab[i]} exploded')
        shahab = shahab[:i-1] + [ree] + shahab[i+1:]
    else:
        print(f'step {count}: meteorite with index {i-1} with size {shahab[i-1]} exploded')
        i -= 1
        shahab = shahab[:i] + [ree] + shahab[i+2:]
        

while i < len(shahab):
    if shahab[i-1] > 0 and shahab[i] < 0:
        ree = shahab[i-1] + shahab[i]
        if shahab[i-1] != -shahab[i]:
            check()
            
        else:
            print(f'step {count}: meteorite with index {i-1} and {i} with size {shahab[i-1]} exploded')
            shahab = shahab[:i-1] + shahab[i+1:]
            i -= 1

        print(
            'new orbit:',
            shahab
            )
        count += 1
        
    else:
        i += 1

print('final orbit:', shahab)