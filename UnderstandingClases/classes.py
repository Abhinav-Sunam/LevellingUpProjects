#understanding OOPs/Classes
class Person:
    def __init__(self, name, age):
        # Variables that MUST be initialized in __init__
        self.name = name  # Core attribute: Every person has a name
        self.age = age    # Core attribute: Every person has an age

    def introduce(self):
        # Method using the initialized attributes
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def set_favorite_food(self, food):
        # Variable created dynamically in this method
        self.favorite_food = food  # Only relevant after calling this method
        print(f"{self.name}'s favorite food is now set to {food}.")

    def show_favorite_food(self):
        # Check if the dynamically created variable exists
        if hasattr(self, 'favorite_food'):  # Check if favorite_food exists
            print(f"{self.name}'s favorite food is {self.favorite_food}.")
        else:
            print(f"{self.name} has no favorite food set yet!")

person = Person("Alice", 25) #creating an object
person.introduce()
person.show_favorite_food()
person.set_favorite_food("Pizza")
person.show_favorite_food()



class TicTacToe:
    def __init__(self):
        self.board=[' ' for _ in range(9)]
        self.current_winner=None
    def print_board(self):
        prboard=[[str(i) for i in range((j*3),((j+1)*3))] for j in range(3)]
        for x in prboard:
            print("| "+ " | " .join(x)+" |")
           # print('| ' + ' | '.join(row), ' |') 

game=TicTacToe()
game.print_board()