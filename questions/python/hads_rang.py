colors_codes = {    
    "Red": {"R": 255, "G": 0,"B": 0},    
    "SlateBlue": {"R": 106, "G":90, "B": 205},   
    "DarkOrange": {"R": 255, "G": 140, "B": 0},
    "MediumSpringGreen": {"R": 0,"G": 250, "B": 154},
    "DarkViolet": {"R": 148, "G": 0, "B": 211},
    "Gold": {"R": 255, "G": 215, "B": 0}  
}

def distance(color1, color2):
    #print(color1['R'], color2['R'])
    return ((color1['R']-color2['R']) ** 2 + (color1['G']-color2['G']) ** 2 + (color1['B']-color2['B']) ** 2) ** 1/2

colors = {"R": int(input()), "G": int(input()), "B": int(input())}
#print(colors)

min_distance = float('inf')
nearest_color = None
for name, values in colors_codes.items():
    #print(name, values)
    dist = distance(colors, values)

    if dist == min_distance:
        nearest_color = None  

    elif dist < min_distance:
        min_distance = dist
        nearest_color = name
   
print(nearest_color)
