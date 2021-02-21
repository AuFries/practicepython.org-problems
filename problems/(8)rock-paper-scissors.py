'''
Exercise 8
A randomized rock paper scissors game, first to 3 wins
'''
import random

def get_key(val): #finds the key associated with a value
    for key, value in rpc.items(): #returns tuple, key, value
        if val == value:
            return key
    return "Key does not exist"

rpc = {1 : 'r', 2 : 's', 3 : 'p'}
player_wins = 0
PC_wins = 0

while player_wins <= 2 and PC_wins <= 2:
    player_choice = input("Enter rock, paper, or scissors (r/p/s): ")
    PC_choice = random.randint(1,3)
    print("The computer chose:", rpc[PC_choice])

    if get_key(player_choice)+1 == PC_choice or (get_key(player_choice) == 3 and PC_choice == 1): #Player beats PC
        player_wins += 1
        print("{c1} beats {c2}, the score is {s1} to {s2}".format(c1 = player_choice, c2 = rpc[PC_choice], s1 = player_wins, s2 = PC_wins))
    elif PC_choice+1 == get_key(player_choice) or (PC_choice == 3 and get_key(player_choice) == 1):
        PC_wins += 1
        print("{c1} beats {c2}, the score is {s1} to {s2}".format(c1 = rpc[PC_choice], c2 = player_choice, s1 = player_wins, s2 = PC_wins))
    else:
        print("Stalemente! The score is {s1} to {s2}".format(s1 = player_wins, s2 = PC_wins))
    print()


if player_wins > PC_wins:
    print("The player wins!")
else:
    print("The PC wins!")
