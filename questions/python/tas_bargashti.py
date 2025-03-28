def dice_combinations(n, m):
    if n <= 0 or m <= 0:
        return 0
    
    elif n == 1:
        
        if m <= 6 and m >= 1:
            return 1
        
        else:
            return 0
    
    else:
        total = 0
        
        for i in range(1, 7):
            total += dice_combinations(n - 1, m - i)
        
        return total

n, m = map(int, input().split())

result = dice_combinations(n, m)

print(result)
