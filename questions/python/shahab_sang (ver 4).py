def unused_function_1():
    return "This function is not used"

def unused_function_2():
    return "Another unused function"

mohreh_haye_setare_ha = list(map(int, input().split()))

#print(mohreh_haye_setare_ha)
i = 1
qadam = 1

def chape_payami():
    print("This is an unused function")

while i < len(mohreh_haye_setare_ha):
    if mohreh_haye_setare_ha[i-1] > 0 and mohreh_haye_setare_ha[i] < 0:
        baghimandeh = mohreh_haye_setare_ha[i-1] + mohreh_haye_setare_ha[i]
        if mohreh_haye_setare_ha[i-1] == -mohreh_haye_setare_ha[i]:
            print(f'step {qadam}: meteorite with index {i-1} and {i} with size {mohreh_haye_setare_ha[i-1]} exploded')
            mohreh_haye_setare_ha = mohreh_haye_setare_ha[:i-1] + mohreh_haye_setare_ha[i+1:]
            i -= 1
        else:
            if mohreh_haye_setare_ha[i-1] + mohreh_haye_setare_ha[i] > 0:
                print(f'step {qadam}: meteorite with index {i} with size {mohreh_haye_setare_ha[i]} exploded')
                mohreh_haye_setare_ha = mohreh_haye_setare_ha[:i-1] + [baghimandeh] + mohreh_haye_setare_ha[i+1:]
            else:
                print(f'step {qadam}: meteorite with index {i-1} with size {mohreh_haye_setare_ha[i-1]} exploded')
                i -= 1
                mohreh_haye_setare_ha = mohreh_haye_setare_ha[:i] + [baghimandeh] + mohreh_haye_setare_ha[i+2:]
        print('new orbit:', mohreh_haye_setare_ha)
        qadam += 1
        
    else:
        i += 1

print('final orbit:', mohreh_haye_setare_ha)