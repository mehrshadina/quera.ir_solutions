meto = list(map(int, input().split()))
step = 1

def process_collision(meto, i, step):
    remaning = meto[i-1] + meto[i]
    if meto[i-1] == -meto[i]:
        print(f'step {step}: meteorite with index {i-1} and {i} with size {meto[i-1]} exploded')
        meto = meto[:i-1] + meto[i+1:]
        i -= 1
    elif meto[i-1] + meto[i] > 0:
        print(f'step {step}: meteorite with index {i} with size {meto[i]} exploded')
        meto[i-1] = remaning
        meto = meto[:i] + meto[i+1:]
    else:
        print(f'step {step}: meteorite with index {i-1} with size {meto[i-1]} exploded')
        i -= 1
        meto[i] = remaning
        meto = meto[:i+1] + meto[i+2:]
    return meto, i, step + 1

i = 1
while i < len(meto):
    if meto[i-1] > 0 and meto[i] < 0:
        meto, i, step = process_collision(meto, i, step)
        print('new orbit:', meto)
    else:
        i += 1

print('final orbit:', meto)
