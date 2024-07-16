import random

class SnakeWaterGunGame:
    def __init__(self):
        self.choices = {1: "Snake", -1: "Water", 0: "Gun"}
        self.youDict = {"s": 1, "w": -1, "g": 0}
        self.computer_choice = random.choice([-1, 0, 1])
    
    def get_user_choice(self):
        youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
        self.user_choice = self.youDict.get(youstr)
        if self.user_choice is None:
            print("Invalid choice. Please enter 's', 'w', or 'g'.")
            return False
        return True
    
    def determine_winner(self):
        print(f"You chose {self.choices[self.user_choice]}")
        print(f"Computer chose {self.choices[self.computer_choice]}")
        
        if self.computer_choice == self.user_choice:
            print("It's a draw!")
        else:
            if self.computer_choice == -1 and self.user_choice == 1:
                print("You win!")
            elif self.computer_choice == -1 and self.user_choice == 0:
                print("You lose!")
            elif self.computer_choice == 1 and self.user_choice == -1:
                print("You lose!")
            elif self.computer_choice == 1 and self.user_choice == 0:
                print("You win!")
            elif self.computer_choice == 0 and self.user_choice == -1:
                print("You win!")
            elif self.computer_choice == 0 and self.user_choice == 1:
                print("You lose!")
            else:
                print("Something went wrong!")
    
    def play(self):
        if self.get_user_choice():
            self.determine_winner()

# Create an instance of the game and play
game = SnakeWaterGunGame()
game.play()
