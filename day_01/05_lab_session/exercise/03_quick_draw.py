from random import choice

options = ["Rock", "Paper", "Scissors"]

def select_user_choice():
    while True:
        user_choice = input("Pick a choice (Rock/Paper/Scissors): ")
        if user_choice in options:
            return user_choice

def select_cpu_choice():
    return choice(options)

def game_winner(player, cpu):
    if player == cpu:
        return "Draw"
    elif (
            (player == "Scissors" and cpu == "Paper") or
            (player == "Rock" and cpu == "Scissors") or
            (player == "Paper" and cpu == "Rock")
    ):
        return "Player"
    else:
        return "CPU"


def RPS_game():
    player_select = select_user_choice()
    cpu_select = select_cpu_choice()
    winner = game_winner(player_select,cpu_select)

    print(f"Player picked {player_select}, CPU picked {cpu_select}")
    if winner == "Draw":
        print("It's a DRAW")
    else:
        print(winner, "wins")


RPS_game()