import random
import time

# Define the list of colors
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

# Function to display a random color and get player input
def display_color_and_guess():
    # Choose a random color
    color = random.choice(colors)
    print("Color:", color)
    
    # Start the timer
    start_time = time.time()
    
    # Get player input with a timeout of 10 seconds
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 10:
            print("Time's up!")
            return None
        try:
            guess = input("Your guess: ").lower()
            if guess == color:
                return color
            else:
                return None
        except EOFError:
            pass

# Main function to play the game
def play_game():
    score = 0
    
    # Start the timer for the game (50 seconds)
    start_time = time.time()
    while time.time() - start_time < 50:
        print("\nGet ready for the next color!")
        time.sleep(1)
        print("Go!")
        time.sleep(1)
        result = display_color_and_guess()
        if result:
            print("Correct!")
            score += 5
    
    print("\nGame over!")
    print("Your final score is:", score)

# Run the game
play_game()