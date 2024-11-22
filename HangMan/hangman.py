import random
from words import engwords
import string
#meaning from words.py import words variable

#function to make sure the random word chosen by the computer does not have a space or - in between
def get_valid_word(words):
    word=random.choice(words) #gets word randomly
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

#main game
def hangman():
    word = get_valid_word(engwords)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters=set()
     
    lives=10
    while ((len(word_letters))>0 and lives>0):  
     #lettters used
     print(f"You have {lives} lives left and you have used these letters: ", " ".join(used_letters))

     #what current word is
     word_list=[letter if letter in used_letters else '-' for letter in word]
     print("Current word: ", " ".join(word_list ))
     user_letter=input("Guess a letter: ").upper()
     if user_letter in alphabet - used_letters:
         used_letters.add(user_letter)
         if user_letter in word_letters:
             word_letters.remove(user_letter)
         else:
              lives=lives-1
              print("Letter not in word.")

     elif user_letter in used_letters:
                 print("You have already used that character. Please try again.")
     else:
          print("INVALID CHARACTER!")            
    if(lives==0):
         print(f"Sorry you died! The word was {word}")
    else:
         print(f"YAYYY you guessed the word {word} correctly")
         print()

hangman()