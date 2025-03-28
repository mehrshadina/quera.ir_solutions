def process_explosion(jesm, index, step, is_same_size=False):
    if is_same_size:
        print(f'step {step}: meteorite with index {index-1} and {index} with size {jesm[index-1]} exploded')
        jesm.pop(index)
        jesm.pop(index-1)
    else:
        remaning = jesm[index-1] + jesm[index]
        if remaning > 0:
            print(f'step {step}: meteorite with index {index} with size {jesm[index]} exploded')
            jesm[index-1] = remaning
            jesm.pop(index)
        else:
            print(f'step {step}: meteorite with index {index-1} with size {jesm[index-1]} exploded')
            jesm[index] = remaning
            jesm.pop(index-1)
    return jesm

def handle_collisions(jesm):
    i = 1
    step = 1
    while i < len(jesm):
        if jesm[i-1] > 0 and jesm[i] < 0:
            if jesm[i-1] == -jesm[i]:
                jesm = process_explosion(jesm, i, step, is_same_size=True)
            else:
                jesm = process_explosion(jesm, i, step)
            print('new orbit:', jesm)
            step += 1
            i = max(i-1, 1)
        else:
            i += 1
    return jesm


jesm = list(map(int, input().split()))
final_orbit = handle_collisions(jesm)
print('final orbit:', final_orbit)
