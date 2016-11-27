

def count_games(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        list_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') # separate each game with its properties to separate list 
            list_games.append(game) # creates one list with all information kept in lists
            x += 1
        hm_games = len(list_games)
        return hm_games   
       
def decide(data_file_name, year):
      with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        year_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') 
            year_games.append(game[2]) # Puts all the years in a list
            x += 1
        if year in year_games: 
            return True
        else:
            return False
        
        
def get_latest(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = read_stat.split('\n')
        year_games = []
        title_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') 
            year_games.append(game[2]) # list of years
            title_games.append(game[0]) # list of game titles
            x += 1
        for i in year_games:
            i = int(i)                      # each index convert to integer
        max_year = str(max(year_games))     # need to convert to string to compare with the values from year_games list
        x = 0
        for i in year_games:
            if year_games[x] == max_year:   
                return title_games[x]
            x += 1
                
        
def count_by_genre(data_file_name, genre):
 with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = read_stat.split('\n')
        genre_games = []
        list_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t') 
            genre_games.append(game[3]) # create list with game genres
            x += 1
        game_num = 0
        for i in genre_games:   # loop through the list with genres 
            if genre == i:
                game_num += 1   # increment when found the proper genre
            else:
                pass
        return game_num            
           
        
def get_line_number_by_title(data_file_name, title):
     with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        title_games = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t')  
            title_games.append(game[0]) # title list 
            x += 1
        try:
            x = 0
            while x <= len(title_games):   # go through the title_games
                if title == title_games[x]:  
                    break                 # if found the proper title, breaks the loop end return the line index
                else:
                    pass
                x += 1  
            return x+1
        except IndexError:
            return 'That was invalid value, try again :)'  # If user input is not from list

def sort_abc(data_file_name):
    with open('game_stat.txt', newline='') as game_stat:        
        read_stat = game_stat.read()
        splited_read_stat = game_read_stat = read_stat.split('\n')
        title_games = []
        title_games_abc = []
        x = 0        
        for game in range(len(splited_read_stat)-1):            
            game = splited_read_stat[x].split('\t')  
            title_games.append(game[0]) # title list 
            title_games_abc.append(game[0][0]) # list with first letters of the games titles
            x += 1
        
        sorted_games = []
        for game in range(len(title_games)):         
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
            game = splited_read_stat[x].split('\t') 
            if game[3] not in genre_games: # condition for not duplicating values
                genre_games.append(game[3]) # game[3] - where are the genres
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
            game = splited_read_stat[x].split('\t') 
            genre_games.append(game[3]) # genre list 
            sell_games.append(game[1]) 
            if game[3] == prop_genre: # Only games with the accurate genre are added to the list
                sell_genre[float(game[1])] = (game[0])
            else:
                pass
            x += 1
        list_of_games = list(sorted(sell_genre)) # sell values are sorted and converted to list, the biggest sells are last
        return sell_genre.get(list_of_games[-1])
      
