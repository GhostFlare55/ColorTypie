import random
import time

#list of colors randomly shuffled
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Getting the player's input
def display_color_and_guess():
    # Random color Generator
    color = random.choice(colors)
    print("Color:", color) 
    # TIMER
    start_time = time.time()
    
    # Get player input with a timeout of 3 seconds
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 3:
            print("Time's up!")
            return None
        try:
            guess = input("Type it quickly: ").lower()
            if guess == color:
                return color
            else:
                return None
        except EOFError:
            pass

def play_game():
    score = 0
    
    # Starting the 60 seconds timer (Duration of the game)
    start_time = time.time()
    while time.time() - start_time < 60:
        print("\nGet ready to type the next color!")
        time.sleep(1)
        print("Go!")
        time.sleep(1)
        result = display_color_and_guess()
        if result:
            print("Correct!")
            score += 1
        else: 
            print("Wrong!")
            score += 0
            
    print("\nTime's Up! Game Over!")
    print("Here is your final score:", score)

play_game()