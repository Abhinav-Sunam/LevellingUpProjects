import random

def guess(x):
    random_number= random.randint(1,x)
    guess=0 #we dont want guess to be equal to the random number wihtout the user inputting 
    while(guess!=random_number):
        guess=int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if(guess<random_number):
            print("Sorry, guess again. Too low.")
        elif (guess>random_number):
            print("Sorry, guess again. Too high.")
    print(f"Yayyyy, congarts!!! You have guessed the number {random_number}")        

def computer_guess(x):
    low=1
    high=x
    feedback=''
    while(feedback!='c'):
      if low!=high:
          guess=random.randint(low,high)
      else:
          guess=low
      feedback=input(f"Is {guess} too high(H) or too low(L) or correct(C)").lower() # makes all lower case
      if feedback=='h':
          high=guess-1
      elif feedback=='l':
          low=guess+1

    print(f"Yayy! The computer guessed your number, {guess}, correctly")

print("YOU GUESS THE NUMBER HEHE: ")
guess(10)
print("")
print("")
print("COMPUTER GUESSING: ")
computer_guess(900)