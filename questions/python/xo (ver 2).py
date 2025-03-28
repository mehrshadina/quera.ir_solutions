import os
import time

player_1 = "X"
player_2 = "O"

turn = 1
game_on = True

moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def welcome_message():
    os.system('clear')
    print("========================")
    print("=== LET'S PLAY A GAME ===")
    print("========================")
    time.sleep(3)

def print_board():
    os.system('clear')
    print(f" {moves[0]} | {moves[1]} | {moves[2]} ")
    print("-----------")
    print(f" {moves[3]} | {moves[4]} | {moves[5]} ")
    print("-----------")
    print(f" {moves[6]} | {moves[7]} | {moves[8]} ")
    print("=============")

def player_pick():
    global turn
    if turn % 2 == 0:
        play = player_2
        square = input("PLAYER 2 PICK A SQUARE: ")
    else:
        play = player_1
        square = input("PLAYER 1 PICK A SQUARE: ")

    if not square.isdigit() or int(square) < 1 or int(square) > 9 or not isinstance(moves[int(square) - 1], int):
        print("Not a valid square.")
        player_pick()
    else:
        moves[int(square) - 1] = play
        turn += 1

def check_match(a, b, c):
    global game_on
    if moves[a] == moves[b] == moves[c]:
        game_on = False
        if moves[a] == player_1:
            print("Player one wins!")
        else:
            print("Player two wins!")

def check_winner():
    global game_on
    if not game_on:
        return

    check_match(0, 1, 2)
    if not game_on:
        return
    check_match(3, 4, 5)
    if not game_on:
        return
    check_match(6, 7, 8)
    if not game_on:
        return
    check_match(0, 4, 8)
    if not game_on:
        return
    check_match(2, 4, 6)
    if not game_on:
        return
    check_match(0, 3, 6)
    if not game_on:
        return
    check_match(1, 4, 7)
    if not game_on:
        return
    check_match(2, 5, 8)
    if not game_on:
        return

    if turn > 9:
        game_on = False
        print("It's a draw!")

welcome_message()
print_board()
while game_on:
    player_pick()
    print_board()
    check_winner()

