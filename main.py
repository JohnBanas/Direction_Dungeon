# This is a sample Python script.
from art import *
# Main menu Ascii art
tprint(" Welcome to Direction Dungeon! ", font="fancy2", chr_ignore=True, decoration="wave3")
print(" ")
# Text for main title "fancy4" decoration="wave3"
aprint("sword2")
tprint(" Enter a number for the options below: ", font="fancy4", chr_ignore=True)
aprint("sword2")
print(" ")

option = input('''1. New Game 
2. Leaderboards 
''')


def show_menu(choice):
    if choice == '1':
        print('You have selected a new game.')
        # game_start()
    else:
        print('You have selected leaderboards.')
        # leaderboard()


show_menu(option)








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
