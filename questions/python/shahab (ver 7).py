def handle_collisions(nuc):
    step = 1
    i = 1
    while i < len(nuc):
        if nuc[i-1] > 0 and nuc[i] < 0:
            if nuc[i-1] == -nuc[i]:
                print(f'step {step}: meteorite with index {i-1} and {i} with size {nuc[i-1]} exploded')
                nuc.pop(i)
                nuc.pop(i-1)
                i -= 1
            elif nuc[i-1] + nuc[i] > 0:
                print(f'step {step}: meteorite with index {i} with size {nuc[i]} exploded')
                nuc[i-1] += nuc[i]
                nuc.pop(i)
            else:
                print(f'step {step}: meteorite with index {i-1} with size {nuc[i-1]} exploded')
                nuc[i] += nuc[i-1]
                nuc.pop(i-1)
                i -= 1
            step += 1
            print('new orbit:', nuc)
        else:
            i += 1
        i = max(i, 1)
    return nuc

print('final orbit:', handle_collisions(list(map(int, input().split()))))
