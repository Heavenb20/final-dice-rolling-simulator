import random

def roll_dice(player_name):
    """
    Simulate rolling a dice (1 to 6) and return the result as a tuple.

    Args:
        player_name (str): The name of the player rolling the dice.

    Returns:
        tuple: A tuple containing the player's name and the dice roll.
    """
    roll_result = random.randint(1, 6)
    return (player_name, roll_result)

def log_rolls_to_file(rolls):
    """
    Log the dice rolls to a text file.

    Args:
        rolls (list of tuples): List of tuples with player name and roll results.
    """
    try:
        with open("dice_rolls.txt", "w") as file:
            for roll in rolls:
                file.write(f"{roll[0]} rolled a {roll[1]}\n")
        print("Game results have been saved to 'dice_rolls.txt'.")
    except Exception as e:
        print("An error occurred while saving the game results:", e)

def main():
    """
    Main function to run the Dice Rolling Simulator game.
    """
    print("Welcome to the Dice Rolling Simulator!")
    
    player_name = input("Enter your name: ").strip()  # Ask for the player's name
    rolls = []  # List to store all rolls

    while True:
        try:
            user_input = input("Type 'roll' to roll the dice or 'quit' to exit: ").strip().lower()

            if user_input == 'roll':
                result = roll_dice(player_name)  # Roll the dice
                rolls.append(result)  # Store the result in the list
                print("{} rolled a {}".format(result[0], result[1]))
            elif user_input == 'quit':
                print("Thanks for playing!")
                print("Game Summary:")
                for roll in rolls:
                    print("{} rolled a {}".format(roll[0], roll[1]))
                log_rolls_to_file(rolls)  # Save results to file
                break
            else:
                print("Invalid input! Type 'roll' or 'quit'.")
        except Exception as e:
            print("An unexpected error occurred:", e)

main()

