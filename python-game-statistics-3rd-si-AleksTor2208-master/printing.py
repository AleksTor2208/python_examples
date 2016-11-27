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
    print('The output of count_games function is: ', end='') 
    b(count_games('game_stat.txt'))
    os.system('clear')
    x = input('To get the output from the decide function type the year of the game release _')
    b(decide('game_stat.txt', x))
    print('The latest game in list is: ', end='') 
    b(get_latest('game_stat.txt'))
    os.system('clear')
    x = input('Type the genre here: ')
    print('The amount of %s games is  ' % x, end='') 
    b(count_by_genre('game_stat.txt', x))
    os.system('clear')
    x = input('Type the title of the game here: ')
    print('%s is on the line: ' % x, end='')
    b(get_line_number_by_title('game_stat.txt', x))
    print('There is a sorted list of games ', end='') 
    b(', '.join(sort_abc('game_stat.txt')))
    print('Genres: ', end='') 
    b(', '.join(get_genres('game_stat.txt')))
    print('Best seller among "First-person shooter" is: ', end='') 
    b(when_was_top_sold_fps('game_stat.txt'))
    
    

main()