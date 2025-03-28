import ast

input_data = input()
players = ast.literal_eval(input_data)

team_players = {}
for player in players:
    club = player['club']
    age = player['age']
    if club not in team_players:
        team_players[club] = {'under_25': 0, 'total': 0}
    team_players[club]['total'] += 1
    if age < 25:
        team_players[club]['under_25'] += 1

teams = []
for player in players:
    if player['club'] not in teams:
        teams.append(player['club'])

max_under_25 = max(
    (data['under_25'] for data in team_players.values()), 
    default=0
)

top_teams = [
    team 
    for team, data in team_players.items() 
    if data['under_25'] == max_under_25 and max_under_25 > 0
]


if max_under_25 == 0:
    message = "Mr.Ghalenoei says : Our clubs should be producing more high quality young players."
else:
    if len(top_teams) == 1:
        message = f"Mr.Ghalenoei says : Thank you {top_teams[0]} for producing high quality young players."
    else:
        message = f"Mr.Ghalenoei says : Thank you {', '.join(top_teams[:-1])} and {top_teams[-1]} for producing high quality young players."

print(teams)
print(message)
