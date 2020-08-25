import random
import sys

computer_choices = ['scissors', 'paper', 'rock']
player_scores = {}
current_player = ''
game_score = [50, 100]
default_score = 0


def player_name():
    global current_player
    current_player = input("Enter your name: ")
    print(f"Hello, {current_player}")


def previous_players():
    file = open('rating.txt', 'r')
    players = file.readlines()
    for player in players:
        player_scores[player.split()[0]] = player.split()[1]
    file.close()


def new_player():
    global current_player
    if current_player not in player_scores.keys():
        file = open('rating.txt', 'a')
        file.write(f'{current_player} {str(default_score)}\n')
        file.close()


def player_current_rating():
    global current_player
    rating = player_scores[current_player]
    print(f'Your rating: {rating}')


def draw():
    player_scores[current_player] = int(player_scores[current_player]) + game_score[0]


def win():
    player_scores[current_player] = int(player_scores[current_player]) + game_score[1]


def update_rating_file():
    file = open('rating.txt', 'w')
    file.truncate(0)
    file = open('rating.txt', 'a')
    for key, value in player_scores.items():
        file.write(f'{key} {str(value)}\n')
    file.close()


def game():
    while True:
        player_input = input()
        computer_play = random.choice(computer_choices)
        if player_input == '!rating':
            player_current_rating()
            game()
        if player_input == '!exit':
            print("Bye!")
            sys.exit()
        if player_input != '!rating':
            if player_input != '!exit':
                if player_input not in computer_choices:
                    print("Invalid input")
        if player_input == 'rock':
            if computer_play == 'scissors':
                print("Well done. The computer chose scissors and failed")
                win()
                update_rating_file()
            elif computer_play == 'paper':
                print("Sorry, but the computer chose paper")
            elif computer_play == 'rock':
                print("There is a draw (rock)")
                draw()
                update_rating_file()
        if player_input == 'paper':
            if computer_play == 'rock':
                print("Well done. The computer chose rock and failed")
                win()
                update_rating_file()
            elif computer_play == 'scissors':
                print("Sorry, but the computer chose scissors")
            elif computer_play == 'paper':
                print("There is a draw (paper)")
                draw()
                update_rating_file()
        if player_input == 'scissors':
            if computer_play == 'paper':
                print("Well done. The computer chose paper and failed")
                win()
                update_rating_file()
            elif computer_play == 'rock':
                print("Sorry, but the computer chose rock")
            elif computer_play == 'scissors':
                print("There is a draw (scissors)")
                draw()
                update_rating_file()


player_name()
previous_players()
new_player()
game()
