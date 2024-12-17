import random
import seaborn as sns
import matplotlib.pyplot as plt
import time

def roll_dice():
    # Simulate rolling a dice and return a random number from 1 to 6
    return random.randint(1, 6)

def player_turn(player_num):
    # Ask the player to press Enter to roll the dice
    print(f"Player {player_num}'s turn:")
    input("Press Enter to roll the dice...")  
    roll = roll_dice()
    print(f"Player {player_num} rolled: {roll}")
    return (player_num, roll)

def show_results(players):
    # Display all players' rolls and find the winner
    print("\nResults:")
    for player, roll in players:
        print(f"Player {player} rolled: {roll}")
    
    # Find the player with the highest roll
    winner = max(players, key=lambda x: x[1])
    print(f"\n{winner[0]} wins with a roll of {winner[1]}!")

def plot_rolls(roll_count):
    # Create a bar chart showing the frequency of each dice roll (1-6)
    sns.set(style="darkgrid")
    plt.figure(figsize=(8, 6))
    sns.barplot(x=[1, 2, 3, 4, 5, 6], y=roll_count)
    plt.title("Dice Roll Distribution")
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.show()

def main():
    print("Welcome to the Dice Rolling Simulator!")
    
    # Ask how many players are playing
    num_players = int(input("How many players? "))
    
    players = []
    roll_count = [0] * 6  # Track how often each roll (1-6) occurs
    total_time = 0  # Track how long the game takes

    for i in range(1, num_players + 1):
        # For each player, roll the dice and track the time
        start_time = time.time()
        player, roll = player_turn(i)
        players.append((player, roll))
        roll_count[roll - 1] += 1  # Count the roll
        total_time += (time.time() - start_time)  # Add the time for this player's turn

    # Show the final results
    show_results(players)
    
    # Show the bar chart of dice rolls
    plot_rolls(roll_count)
    
    # Show how long the game took
    print(f"\nTotal time for all turns: {total_time:.2f} seconds")

# Run the game directly (no need for if __name__ block)
main()



