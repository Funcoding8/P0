"""
Attempts to guess the Wordle word by comparing the user's guess to the actual word.

Args:
    guess (str): The 5-letter word the user has guessed.

Returns:
    str: A string of 5 characters representing the correctness of the guess, where:
        'G' means the letter is in the correct position
        'Y' means the letter is in the word but in the wrong position
        '-' means the letter is not in the word
"""
word ="books"

def makeAGuess(guess):

  hint=""
  for i in range(5):
    if guess[i] == word[i]:
      hint.add["G"]
    elif guess[i]== word:
      hint.add["Y"]
    else:
      hint.add["-"]
  retrun(hing)

  print(makeAGuess("books"))
  

def playWordle(word):
    
  print("Let's play wordle! /n Guess the Wordle in 6 tries. Each guess must be a valid 5-letter word. For each guess, a hint will tell you how many letters you've guessed correctly. A G represents a letter in the word and in the correct spot.. A Y represents a letter in the word but in the wrong spot. A - represents a letter not in the word in any spot. \n Guess below! \n")


  i = 1
  while i < 6:
    guess = input("guess a 5 letter word")
    hint = makeAGuess(guess)
    print(hint)
    if hint == "GGGGG":
      print("You win")
      break 
    if hint !="GGGGG":
      print("You lost The word was",word)

