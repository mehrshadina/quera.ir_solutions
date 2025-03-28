number_of_squares = int(input())
used_squares = 0
floor = 0

for i in range(1, number_of_squares+1):
    neaded = 0
    for a in range(1, i+1):
        neaded += a
    #print(neaded)

    used_squares += neaded
    if used_squares <= number_of_squares:
        floor += 1
    else:
        break

print(floor)
