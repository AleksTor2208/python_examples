import os
import time
from reports import count_games, decide, get_latest, count_by_genre, get_line_number_by_title, sort_abc, get_genres, when_was_top_sold_fps

# get_latest count_by_genre
# get_line_number_by_title


func_1 = count_games('game_stat.txt')


def printing_func(function):
    os.system('clear')
    print('\033[36m\033[92m{}\033[0m'.format(function))
    time.sleep(3)
    # os.system('clear')

def main():
    b = printing_func
    # b(count_games('game_stat.txt'))
    # x = input('Type the year of the game release here _')
    # b(decide('game_stat.txt', x))
    # b(get_latest('game_stat.txt'))
    # x = input('Type the genre here: ')
    # b(count_by_genre('game_stat.txt', x))
    # x = input('Type the title of the game here: ')
    # b(get_line_number_by_title('game_stat.txt', x))
    # b(', '.join(sort_abc('game_stat.txt')))
    b(', '.join(get_genres('game_stat.txt')))
    b(when_was_top_sold_fps('game_stat.txt'))

main()