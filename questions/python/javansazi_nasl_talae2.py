import ast

input_data = input()
players = list(ast.literal_eval(input_data))
n = len(players)
for i in range(n):
    for j in range(0, n - i - 1):
        if players[j]['age'] > players[j + 1]['age']:
            # Swap the elements
            players[j], players[j + 1] = players[j + 1], players[j]

print(tuple(players))

