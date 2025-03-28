def read_input():
    return list(map(int, input().split()))

def explode_meteorites(meteorites):
    step = 1
    i = 1
    while i < len(meteorites):
        if meteorites[i-1] > 0 and meteorites[i] < 0:
            meteorites, i = handle_collision(meteorites, i, step)
            step += 1
        else:
            i += 1
    return meteorites

def handle_collision(meteorites, i, step):
    remaining = meteorites[i-1] + meteorites[i]
    if meteorites[i-1] == -meteorites[i]:
        print(f'step {step}: meteorite with index {i-1} and {i} with size {meteorites[i-1]} exploded')
        meteorites = meteorites[:i-1] + meteorites[i+1:]
        i -= 1
    else:
        if remaining > 0:
            print(f'step {step}: meteorite with index {i} with size {meteorites[i]} exploded')
            meteorites = meteorites[:i-1] + [remaining] + meteorites[i+1:]
        else:
            print(f'step {step}: meteorite with index {i-1} with size {meteorites[i-1]} exploded')
            i -= 1
            meteorites = meteorites[:i] + [remaining] + meteorites[i+2:]
    print('new orbit:', meteorites)
    return meteorites, i

meteorites = read_input()
final_orbit = explode_meteorites(meteorites)
print('final orbit:', final_orbit)



