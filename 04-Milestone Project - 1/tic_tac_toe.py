# -*- coding: utf-8 -*- 
"""Tic Tac Toe game

This program is a Tic Tac Toe game which lets the two players play on a single
computer."""
import sys

print("**********************","| Tic    Tac    Toe! |","**********************",sep="\n")

stay_in_intro = True
while stay_in_intro:
    response = input("Are you ready to start [y/n]? ")
    if response.lower() == "y":
        stay_in_intro = False
    elif response.lower() == "n":
        print("See you later then!")
        sys.exit(0)
    else:
        print("Seems like you've entered an unvalid option. Let's try again!\n")

# FIXME: Allow players to choose
player_1_marker = "X"
player_2_marker = "O"
    
board = {1:"1",2:"2", 3:"3",4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

def print_board():
    print("\n"
        "   |   |   ",
        f" {board[7]} | {board[8]} | {board[9]} ",
        "   |   |   ",
        "-"*12,
        "   |   |   ",
        f" {board[4]} | {board[5]} | {board[6]} ",
        "   |   |   ",
        "-"*12,
        "   |   |   ",
        f" {board[1]} | {board[2]} | {board[3]} ",
        "   |   |   ",
        sep="\n"
        )


replay = True
while replay:
    print_board()
    player_1_choice = input("\nPlayer 1, choose your next position (1-9):" )
    player_1_choice = int(player_1_choice) if player_1_choice.isnumeric() else 0
    if player_1_choice in range(1,10):
        if board[player_1_choice] == player_1_marker:
            print("You've already put a marker on that cell. Try again.")
            continue
        elif board[player_1_choice] == player_2_marker:
            print("Player 2 has already put a marker on that cell. Try again.")
            continue
        else:
            board[player_1_choice] = player_1_marker
            # Verify if win
            print_board()
    else:
        print("Seems like you've entered an unvalid option. Let's try again!")
        continue
    move_on = False
    while not move_on:
        player_2_choice = input("\nPlayer 2, choose your next position:" )
        player_2_choice = int(player_2_choice) if player_2_choice.isnumeric() else 0
        if player_2_choice in range(1,10):
            if board[player_2_choice] == player_2_marker:
                print("You've already put a marker on that cell. Try again.")
                print_board()
            elif board[player_2_choice] == player_1_marker:
                print("Player 1 has already put a marker on that cell. Try again.")
                print_board()
            else:
                board[player_2_choice] = player_2_marker
                # Verify if win
                move_on = True
        else:
            print("Seems like you've entered an unvalid option. Let's try again!")
