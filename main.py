import random
import matplotlib.pyplot as plt


def playGame(gameLimit=1_000, ballAmount=1):
    # Create our bag
    bag = ['red', 'blue']  # Starts with a red and blue marble
    # Count the number of moves
    moveCount = 0

    # Loop until we break
    while True:
        # Increment the move count
        moveCount += 1
        # Draw a ball!
        ball = random.choice(bag)

        # If the ball is blue, we can stop
        if ball == 'blue':
            break

        # Otherwise, we'll have to append another n red balls
        for _ in range(ballAmount):
            bag.append('red')

        # Stop at the game limit
        if moveCount >= gameLimit:
            break

    # Return the number of moves
    return moveCount


# Driver code
if __name__ == '__main__':
    # Let's play n games!
    gameCount = 1_000_000
    gameLimit = 75
    ballAmt = 3

    # Create a histogram of the results
    results = [playGame(gameLimit, ballAmt) for _ in range(gameCount)]
    plt.hist(results, bins=100)
    plt.title(f'Number of moves to draw a blue ball (n={gameCount})')
    plt.show()
