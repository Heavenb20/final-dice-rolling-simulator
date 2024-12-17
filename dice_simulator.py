import random

def roll_dice(player_name):
    """
    Simulate rolling a dice (1 to 6) and return the result as a tuple.

    Args:
        player_name (str): The name of the player rolling the dice.

    Returns:
        tuple: A tuple containing the player's name and the dice roll.
    """
    # Generate a random number between 1 and 6 to simulate a dice roll
    roll_result = random.randint(1, 6)
    return (player_name, roll_result)

def log_rolls_to_file(rolls):
    """
    Log the dice rolls to a text file.

    Args:
        rolls (list of tuples): List of tuples with player name and roll results.
    """
    try:
        # Open the file in write mode and save the rolls
        with open("dice_rolls.txt", "w") as file:
            for roll in rolls:
                # Write each roll result in a readable format
                file.write(f"{roll[0]} rolled a {roll[1]}\n")
        print("Game results have been saved to 'dice_rolls.txt'.")
    except Exception as e:
        print(f"An error occurred while saving the game results: {e}")

def main():
    """
    Main function to run the Dice Rolling Simulator game.
    """
    print("Welcome to the Dice Rolling Simulator!")
    
    # Get the player's name
    player_name = input("Enter your name: ").strip()
    rolls = []  # List to store all rolls

    while True:
        try:
            # Ask the user for input to roll the dice or quit the game
            user_input = input("Type 'roll' to roll the dice or 'quit' to exit: ").strip().lower()

            if user_input == 'roll':
                result = roll_dice(player_name)  # Roll the dice
                rolls.append(result)  # Store the result in the list
                print(f"{result[0]} rolled a {result[1]}")
            elif user_input == 'quit':
                print("Thanks for playing!")
                print("Game Summary:")
                # Display the summary of all rolls
                for roll in rolls:
                    print(f"{roll[0]} rolled a {roll[1]}")
                log_rolls_to_file(rolls)  # Save results to file
                break  # Exit the game loop
            else:
                print("Invalid input! Type 'roll' or 'quit'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Call the main function to start the game
main()


