
# How many games are in the file?
def count_games(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        # splited_read_stat = list(read_stat.split(' '))
        # print(splited_read_stat[0].split('\t'))
        # print(read_stat)
        list_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            list_games.append(game) # one list with all information kept in lists
            x += 1
        # for i in list_games:
        #     print(', '.join(i))
        hm_games = len(list_games)
        return hm_games   

# 

#   
       
def decide(data_file_name, year):
      with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        year_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            year_games.append(game[2]) # one list with all information kept in lists
            x += 1
        # print(year_games)
        # year = input('Type the year: _')
        if str(year) in year_games:
            return True
        else:
            return False
        
        
# print(decide('game_stat.txt', 1984))

def get_latest(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = read_stat.split('\n')
        year_games = []
        title_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            year_games.append(game[2]) # all years of launching games kept in a list
            title_games.append(game[0])
            x += 1
        for i in year_games:
            i = int(i)
        max_year = str(max(year_games))
        x = 0
        for i in year_games:
            if year_games[x] == max_year:
                return title_games[x]
            x += 1
        # print(year_games[x])
        
        # while x <= len(year_games):
            # if max_year == year_games[x]:
            #     print(title_games)
            #     break
            # else:
            #     pass

        

# print(get_latest('game_stat.txt'))
        
        
def count_by_genre(data_file_name, genre):
 with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = read_stat.split('\n')
        genre_games = []
        list_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            genre_games.append(game[3]) # create list with game titles
            list_games.append(game)
            x += 1
        game_num = 0
        # if genre in list_games:
        for i in genre_games:
            if genre == i:
                game_num += 1
            else:
                pass
        return game_num            
        # else:
        #     print('There is no such game in list')  

# print(count_by_genre('game_stat.txt', 'RPG'))     
        
def get_line_number_by_title(data_file_name, title):
     with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        title_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            title_games.append(game[0]) # title list 
            x += 1
        try:
            x = 0
            while x <= len(splited_read_stat)-1:
                if title == title_games[x]:
                    break
                else:
                    pass
                x += 1  
            return x+1
        except IndexError:
            return 'That was invalid value, try again :)'

def sort_abc(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        title_games = []
        title_games_abc = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            title_games.append(game[0]) # title list 
            title_games_abc.append(game[0][0]) # list with first letters of the games titles
            x += 1
        # return title_games
        sorted_games = []
        for game in range(len(title_games)): 
        # for game in range(4):
            smallest = min(title_games_abc)
            sorted_games.append(title_games[title_games_abc.index(smallest)])
            x = title_games_abc.index(smallest)
            title_games_abc.pop(x)
            title_games.pop(x) 
        return sorted_games

def get_genres(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        genre_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            if game[3] not in genre_games:
                genre_games.append(game[3]) # title list 
            else:
                pass
            x += 1
        return sorted(genre_games)
        

def when_was_top_sold_fps(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        genre_games = []
        sell_games = []
        title_games = []
        x = 0  
        sell_genre = {}   
        prop_genre = 'First-person shooter'   
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            genre_games.append(game[3]) # genre list 
            sell_games.append(game[1]) 
            if game[3] == prop_genre: # Only games with the accurate genre are added to the list
                sell_genre[float(game[1])] = (game[0])
            else:
                pass
            # list with inf about sells in float
            # title_games.append(game[0])
            x += 1
        list_of_games = list(sorted(sell_genre)) # sell values are sorted and converted to list, the biggest sells are last
        return sell_genre.get(list_of_games[-1])
        # sell_genre(str(list_of_games[-1]))
        
        # x = max(sell_games)
        # return genre_games[sell_games.index(x)]
        # return max(sell_games)
        # step = len(sell_games)
        # # return genre_games[sell_games.index(max(sell_games))]
        # for i in range(step):
        #     if genre_games[sell_games.index(max(sell_games))] = genre:                
        #         sell_games.remove(max(sell_games))
        #         print(max(sell_games))
        #         step -= 1
        #     else:
        #         return genre_games[max(sell_games)]
        #         break


print(when_was_top_sold_fps('game_stat.txt'))


