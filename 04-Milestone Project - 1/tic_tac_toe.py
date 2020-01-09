# -*- coding: utf-8 -*- 
"""Tic Tac Toe game

This program is a Tic Tac Toe game which lets the two players play on a single
computer."""
import art
import random
import sys

board = {1:"1",2:"2", 3:"3",4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}

markers = {1:'', 2:''}
turn_order = []

def print_board():
    """Print the current state of the board"""
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

def player_1_marker_input():
    undecided = True
    while undecided:
        marker = input('Player 1, choose your marker [X/O]: ')
        if marker in {'X','O'}:
            return marker
        if marker.upper() in {'X','O'}:
            return marker.upper()
        else:
            print("Seems like you've entered an unvalid option. Let's try again!")

def player_position_input(player_number):
    undecided = True
    while undecided:
        pos = input(f'Player {player_number}, choose your move [1 to 9]: ')
        if pos.isnumeric():
            if int(pos) in range(1,10):
                undecided = False
            else:
                print("Out of range. Let's try again!")
        else:
            print("Seems like you've entered an unvalid option. Let's try again!")
    return int(pos)

def position_available(pos):
    return not board[pos] in {'X','O'}

def win_check(mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the left side
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def choose_first():
    player_number = random.randint(1,2)
    return player_number

def full_board_check():
    """If board is full, return True"""
    return {"X","O"} == set().union(*board.values())

if __name__ == "__main__":
    
    # Display the game's name
    Art = art.text2art("*************\n"+"| Tic    Tac    Toe! |\n"+"*************\n", font="standard")
    print(Art)

    win_Art = art.text2art("WIN", font="starwars")

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


    while True:    
        markers[1] = player_1_marker_input()
        markers[2] = 'O' if markers[1] == 'X' else 'X'

        turn_order.append(choose_first())
        turn_order.append(2 if turn_order[0] == 1 else 1)

        print(f"Player {turn_order[0]} goes first!")

        replay = True
        while replay:
            print_board()

            first_player = turn_order[0]
            second_player = turn_order[1]


            move_on = False
            while not move_on:
                first_player_choice = player_position_input(first_player)
                if position_available(first_player_choice):
                    board[first_player_choice] = markers[first_player]
                    print_board()
                    move_on = True
                else:
                    if board[first_player_choice] == markers[first_player]:
                        print("You've already put a marker on that cell. Try again.")
                        continue
                    elif board[first_player_choice] == markers[second_player]:
                        print(f"Player {second_player} has already put a marker on that cell. Try again.")
                        continue
            
            if win_check(markers[first_player]):
                print(win_Art)
                print_board()
                print(f"Congratulations, player {first_player}. You have won!")
                break

            if full_board_check():
                print(
                "\nThe board is now full. It's a tie!",
                "Goodbye!",
                sep="\n"
                )
                break

            move_on = False
            while not move_on:
                second_player_choice = player_position_input(second_player)
                if position_available(second_player_choice):
                    board[second_player_choice] = markers[second_player]
                    move_on = True
                else:
                    if board[second_player_choice] == markers[second_player]:
                        print("You've already put a marker on that cell. Try again.")
                        continue
                    elif board[second_player_choice] == markers[first_player]:
                        print(f"Player {first_player} has already put a marker on that cell. Try again.")
                        continue
            
            if win_check(markers[second_player]):
                print(win_Art)
                print_board()
                print(f"Congratulations, player {second_player}. You have won!")
                break
        
        keep_asking = True
        while keep_asking:
            response = input("Do you want to play again [y/n]? ")
            if response.lower() == "y":
                board = {1:"1",2:"2", 3:"3",4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
                keep_asking = False
            elif response.lower() == "n":
                print("See you later then!")
                sys.exit(0)
            else:
                print("Seems like you've entered an unvalid option. Let's try again!\n") 
            