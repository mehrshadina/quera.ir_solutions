def first_sequence(number):
    if number == 0:
        return 5

    else:
        answer = first_sequence(number-1) + number * 7

        return answer


 
def second_sequence(number):
    if number == 0:
        return 1

    elif number == 1:
        return 2

    else:
        answer = (2 * second_sequence(number-1)) - second_sequence(number-2) + number

        return answer


number = int(input())

total = 0
count = 0

for i in range(number):
    num = int(input())
    
    if num % 2 == 0 and num <= 68:
        total = total + first_sequence(num)

    elif num % 2 == 1 and num <= 32:
        total = total + second_sequence(num)

    elif num % 3 == 0:
        total = total + num ** 2

    else:
        count += 1

total = total % 101

print(total)

print(count)
