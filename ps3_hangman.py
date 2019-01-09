# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    fullWord=""
    for i in secretWord:
        if i in lettersGuessed:
            fullWord+= i
    if fullWord == secretWord:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    listWord= list(secretWord)
    count=0
    for i in secretWord:
        if i not in lettersGuessed:
            listWord[count]="_ "
        fullWord = "".join(listWord)
        count+=1
    return fullWord


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alp = "abcdefghijklmnopqrstuvwxyz"
    listAlp =list(alp)
    copyAlp = listAlp[:]
    for i in lettersGuessed:
        if i in copyAlp:
            listAlp.remove(i)
    return ''.join(listAlp)

def humanGraphic(falseCount):
    if falseCount==0:
        print('--------')
        print('|       ')
        print('|       ')
        print('|')
    if falseCount==1:
        print('--------')
        print('|       o')
        print('|       ')
        print('|')
    if falseCount==2:
        print('--------')
        print('|       o')
        print('|       |')
        print('|')
    if falseCount ==3:
        print('--------')
        print('|       o')
        print('|      /|')
        print('|')
    if falseCount ==4:
        print('--------')
        print('|       o')
        print('|      /|\ ')
        print('|')
    if falseCount ==5:
        print('--------')
        print('|       o')
        print("|      /|\ ")
        print('|      / ')
    if falseCount ==6:
        print('--------')
        print('|       o')
        print('|      /|\ ')
        print('|      / \ ')
    if falseCount ==7:
        print('--------')
        print('|     (x )')
        print("|      /|\ ")
        print('|      / \ ' )
    if falseCount ==8:
        print('--------')
        print('|     (xx)')
        print('|      /|\ ')
        print('|      / \ ')
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    #define neccessary variables
    mistakeMade=0
    lettersGuessed=[]
    turn=8
    #print the introductory part of the game
    print('Welcome to the gamec Hangman!')
    print('I am thinking of a word that is '+ str(len(secretWord)) +' letters long')
    print('------------')
    
    #start counting the turn of the game all the way down, starting with turn 8
    
    while turn >0:
        
        #Print ths statement if user wins
        
        if getGuessedWord(secretWord,lettersGuessed) == secretWord:
            print('Congratulations, you won!')
            break
        #Print the number of guess you are having and your available letters to guess
        print('You have '+ str(turn)+ ' guesses left.')
        print('Available letters: '+ getAvailableLetters(lettersGuessed))
        #Define the input of user
        userInput = input('Please guess a letter: ')
        inputLowercase=userInput.lower()
        #Print this statement if user inputs the same guessed word they put before.
        if inputLowercase in lettersGuessed:
            print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))
            print('------------')
        
        #Print this statement if user guesses right
        
        elif inputLowercase in secretWord:
            lettersGuessed.append(inputLowercase)
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
            print('------------')
            
        #Print this statement if user guesses wrong
        
        elif userInput not in secretWord:
            lettersGuessed.append(inputLowercase)
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            mistakeMade+=1
            print(humanGraphic(mistakeMade))
            turn-=1
            print('------------')
        #Print this statement if user uses all 8 guesses
            if mistakeMade == 8:
                print('Sorry, you ran out of guesses. The word was ',secretWord)
                break
            
            
            
                
                
                
                
            





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

wordlist = loadWords()
hangman(chooseWord(wordlist))
