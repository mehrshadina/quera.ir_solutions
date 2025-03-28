numbers = list(map(int , input().split()))
lne_numbers = len(numbers)
sorted_numbers = sorted(numbers)

count = 0

for i in range(lne_numbers):
    if numbers == sorted_numbers:
        print(count)
        break
    else:    
        count += 1
        numbers = numbers[1:] + [numbers[0]]
        #print('here', numbers)
        j = lne_numbers - 1

        
        while numbers[j-1] > numbers[j] and j>0:
            numbers = numbers[:j-1] + [numbers[j]] + [numbers[j-1]] + numbers[j+1:]
            j -= 1
            count +=1

            #print(numbers)

        if j==0:
            print(f'Is not sortable with this algorithm, sorted array: {sorted_numbers}')
            break