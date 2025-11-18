import random
import time

from player import Player
from draw import draw_d20, draw_d6, draw_d4

def print_dramatic_text(text: str, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

if __name__ == '__main__':
    # create character by collecting user input (name + class)
    # print character sheet
    # specify roll that must be beat and enemy initiative by collecting user input
    # any buffs / debuffs?
    # any critical success / failure?

    name = input('Name: ')
    role = input('Role: ')

    player_1 = Player(name, role, 10)

    # player_2 = Player('name', 'role', 'strength')
    # player_2.go()

    score = 0

    print('Your name is ' + player_1.name + ' and your role is ' + player_1.role + '.')
    print_dramatic_text('Welcome to Bludgeons & Flagons!')

    input('Press Enter to roll a d6.')
    roll = random.randint(1, 6)
    draw_d6(roll)
