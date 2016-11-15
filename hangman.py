import random
import sys
capitals = ['Tirana', 'Andorra la Vella', 'Yerevan',   'Vienna',   'Baku',
 'Minsk', 'Brussels', 'Sarajevo', 'Sofia', 'Zagreb', 'Nicosia', 'Prague',
  'Copenhagen', 'Tallinn', 'Helsinki', 'Paris', 'Tbilisi', 'Berlin', 'Athens',
   'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Astana', 'Pristina', 'Riga',
    'Vaduz', 'Vilnius', 'Luxembourg', 'Skopje', 'Valletta',  'Chisinau',
     'Monaco', 'Podgorica', 'Amsterdam', 'Oslo', 'Warsaw', 'Lisbon',
     'Bucharest', 'Moscow', 'San Marino', 'Belgrade', 'Bratislava',
      'Ljubljana', 'Madrid', 'Stockholm', 'Bern', 'Ankara', 'Kyiv',
       'London', 'Vatican']

guess_word = random.choice(capitals)
guess_word = str(guess_word.upper())
global nc_list
nc_list = [] #List which contains uncorect letters ("no characters")
global dash_list 
dash_list = "-" * len(guess_word)
global life
life = ["1", "1", "1", "1", "1"]

def main():
    if len(life) == 0:
        print("Sorry, You have lost.") 
        sys.exit()
    if "-" not in dash_list: #Game won when there are no dashes last
        print("You have won!")
        sys.exit()

    print(dash_list)
    print("Invalid letters:" + str(nc_list))
    print("Lifes:" + str(len(life))) 
    print("")

    question = input("Would you like to guess the letter (type 'letter');\nGuess the whole solution (type 'word')\nor quit (type 'quit')?: ")
    if question == "word": #User can type the whole word or just a letter
        wholeword()
    elif question == "letter": 
        letter()
    elif question == "quit":
        sys.exit()
    elif question == "hax": #Shows the answer
        print(guess_word)
        main()
    else:
        print("Invalid response.")
        print("")
        main()


def wholeword():
    print("")
    wholeword_guess = input("What is the correct answer?: ").upper()#All letters are converted into capital letters
    if wholeword_guess == guess_word: #What happens if user guesses the letter
        print("Your guess is correct, congratulations!")
        sys.exit()
    else:
        life.remove("1") #User losts one life
        print("Sorry, You are not correct.")
    main()


def letter():
    print("")
    letter_guess = input("Choose the letter: ").upper()
    global dash_list
    global nc_list
    global life
    if len(letter_guess) == 1 and letter_guess.isalpha(): #
        if letter_guess in guess_word: #If the letter is correct the function puts the letter into the dush_list
            print("")
            for i in range(0,len(guess_word)): #
                if letter_guess in guess_word:
                    if letter_guess == guess_word[i]:
                        for index, value in enumerate(dash_list): 
                            dash_list = dash_list[:i] + guess_word[i] + dash_list[i+1:] #letter is put into the correct index number
                    else:
                        pass
        else:
            print("Incorrect letter!\n")
            nc_list.append(letter_guess)
            life.remove("1")
            print("")
        main()
    else:
        print("Invalid value")
        main()



print("Welcome to HANGMAN!")
print("")
main()
