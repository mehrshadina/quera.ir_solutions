n = int(input())
spaces = ' ' * int(n/2)
stars = '*'

for i in range(int(n/2)):
    print(spaces + stars + spaces*2 + stars)
    stars += '**'
    spaces = spaces[:-1]

for i in range(int(n/2)+ 1):
    print(spaces + stars + 2*spaces + stars)
    stars = stars[:-2]
    spaces += ' '