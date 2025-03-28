def change_base(number, base):
    result = ""
    
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number //= base
    
    if result != "":
        answer = int(result) if result != "" else 0
    else:
        answer = 0

    return answer

def sum_of_digits(number):
    sum = 0
    for digit in str(number) :
        sum += int(digit)

    return sum

n, m = map(int, input().split())
k = int(input())

max_sum = -2
selected_number = 0

if n < m:
    for num in range(n, m + 1):
        num_in_base_k = change_base(num, k)
        current_sum = sum_of_digits(num_in_base_k)
        
        if current_sum > max_sum or (current_sum == max_sum and num_in_base_k < selected_number):
            max_sum = current_sum
            selected_number = num
else:
    for num in range(m, n + 1):
        num_in_base_k = change_base(num, k)
        current_sum = sum_of_digits(num_in_base_k)
        
        if current_sum > max_sum or (current_sum == max_sum and num_in_base_k < selected_number):
            max_sum = current_sum
            selected_number = num
    

print(selected_number)