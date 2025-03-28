number = int(input())

for i in range(2, int(number/2)):
    if number % i == 0:
        number2 = number
        while 2 <= number2:
            number2 -= 1
            for j in range(2, int(number2/2)):
                if number2 % j == 0:
                    break
            else:
                print(number2, end=' ')
                break

        number2 = number
        while True:
            number2 += 1
            for j in range(2, int(number2/2)):
                if number2 % j == 0:
                    break
            else:
                print(number2)
                break
        break
else:
    print(number)




