counter = 0 
game_on = 0

player_one_name = input("What is your name Player1?: ")
player_two_name = input("What is your name Player2?: ")

one = " "
two = " "
three = " "
four = " "
five = " "
six = " "
seven = " "
eight = " "
nine = " "

def print_board():
  print("\n" + one + " | " + two + " | " + three + "\n" + four +" | " + five + " | " + six + "\n"  + seven + " | " + eight + " | " + nine + "\n________________")



def check_for_win():
  
  #Horizontal win:
  if one == two and two == three and one != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  elif four == five == six and four != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  elif seven == eight == nine and seven != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  #Vertical win:
  elif one == four == seven and one != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  elif two == five == eight and two != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  elif three == six == nine and three != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit() 
  #Diagonal win:
  elif one == five == nine and one != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  elif seven == five == three and seven != " ":
    if counter%2 == 1:
      print("\nHorray, " + player_one_name + " won!")
      print("_____________________________")
      exit()
    else:
      print("\nHorray, " + player_two_name + " won!")
      print("_____________________________")
      exit()
  elif counter == 9:
      print("\nIt's a draw")
      print("____________")
      exit()
  


def print_example_board():
  
  print("\nHere is the template board:")
  print("1" + " | " + "2" + " | " + "3" + "\n" + "4" +" | " + "5" + " | " + "6" + "\n"  + "7" + " | " + "8" + " | " + "9" + "\n")

possible_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print_example_board()
print("Let's begin. " + player_one_name + " starts.")
print_board()

while game_on == 0: 
  while counter%2 == 0:
    move = input(player_one_name + ", choose a field: ")
    if move in possible_inputs:
      #print("Yes good")
      counter += 1
      possible_inputs.remove(move)
      #print(possible_inputs)
      #print(counter)
      if move == "1":
        one = "X"
      elif move == "2":
        two = "X"
      elif move == "3":
        three = "X"
      elif move == "4":
        four = "X"
      elif move == "5":
        five = "X"
      elif move == "6":
        six = "X"
      elif move == "7":
        seven = "X"
      elif move == "8":
        eight = "X"
      elif move == "9":
        nine = "X"
    
      print_board()
      check_for_win()
      continue
    else:
      print("Sorry, but this number is either not available or already taken. Chose another one\n")
      continue

  while counter%2 != 0:
    move = input(player_two_name + ", choose a field: ")
    if move in possible_inputs:
      #print("Yes good")
      counter += 1
      possible_inputs.remove(move)
      #print(possible_inputs)
      #print(counter)
      if move == "1":
        one = "O"
      elif move == "2":
        two = "O"
      elif move == "3":
        three = "O"
      elif move == "4":
        four = "O"
      elif move == "5":
        five = "O"
      elif move == "6":
        six = "O"
      elif move == "7":
        seven = "O"
      elif move == "8":
        eight = "O"
      elif move == "9":
        nine = "O"
      print_board()
      check_for_win()
      continue
    else:
      print("Sorry, but this number is either not available or already taken. Chose another one\n")
      continue