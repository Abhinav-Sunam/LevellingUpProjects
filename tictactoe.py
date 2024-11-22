import random

def play():
    user=input("'r' for rock, 'p' for paper, 's' for scissors: \n").lower()
    computer=random.choice(['r','p','s'])
    print("") #prints an extra line just to make it look goodS
    print(f"Yours is {user} and Opponent's is {computer}")
    if user==computer:
        return 'tie' #we come out of the def after we reach here
    if is_win(user,computer):
         return "YOU WON!!!" #we come out of the def after we reach here
    return 'You Lost' #the only way to reach here is if we lose, i.e. none of the above conditions are true 
    
def is_win(player,opponent):
        if(player=='r' and opponent == 's') or (player=='s' and opponent=='p') \
        or (player=='p'and opponent=='r'):
             return True   
print(play()) 