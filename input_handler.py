def get_user_input():
    """
    Prompts the user for input to roll the dice or quit the game.
    
    Returns:
        str: User input ('roll' or 'quit'). If 'quit', it returns None to signal game exit.
    """
    user_input = input("Type 'roll' to roll the dice or 'quit' to exit: ").lower()
    while user_input not in ['roll', 'quit']:
        print("Invalid input. Please type 'roll' or 'quit'.")
        user_input = input("Type 'roll' to roll the dice or 'quit' to exit: ").lower()
    
    if user_input == 'quit':
        print("Thanks for playing!")
        return None  # Explicitly signal to exit the game
    return user_input

