import random

def roll_dice():
    # Simulate rolling a dice (1 to 6)
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        # Ask user if they want to roll the dice
        user_input = input("Type 'roll' to roll the dice or 'quit' to exit: ").lower()

        if user_input == 'roll':
            print(f"You rolled a {roll_dice()}!")
        elif user_input == 'quit':
            print("Thanks for playing!")
            break
        else:
            print("Invalid input! Type 'roll' or 'quit'.")

if __name__ == "__main__":
    main()
