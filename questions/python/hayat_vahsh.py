eagle = list(map(int, input().split()))
rabbit = list(map(int, input().split()))
mouse = list(map(int, input().split()))
burrow = list(map(int, input().split()))

def distance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

for i in range(20):
    eagle_rabit_distance = distance(eagle[0], eagle[1], rabbit[0], rabbit[1])
    eagle_mouse_distance = distance(eagle[0], eagle[1], mouse[0], mouse[1])
    
    eagle2 = eagle
    if eagle_rabit_distance <= eagle_mouse_distance:
        if eagle[0] > rabbit[0]:
            eagle[0] -= 3 ** 1.2
            rabbit[0] -= 0.5
        else:
            eagle[0] += 1.5
            rabbit += 5
        
        if eagle[1] > rabbit[1]:
            eagle[1] -= 1.5
        else:
            eagle[1] += 1.5

    else:
        if eagle[0] > mouse[0]:
            eagle[0] -= 1.5
        else:
            eagle[0] += 1.5
        
        if eagle[1] > mouse[1]:
            eagle[1] -= 1.5
        else:
            eagle[1] += 1.5



    # eagle 3
    # mouse, rabbit 3   

    eagle[0], eagle[1] = 
