# Pots of Gold Game Problem using Dynamic Programming:


# There are two players, A and B, in Pots of gold game, 
# and pots of gold arranged in a line, each containing some gold coins.
#  The players can see how many coins are there in each gold pot, 
# and each player gets alternating turns in which the player can pick a pot from either end of the line.
#  The winner is the player who has a higher number of coins at the end.
#  The objective is to “maximize” the number of coins collected by A, 
# assuming B also plays “optimally”, and A starts the game.


# Function to maximize the number of coins collected by a player,
# assuming that the opponent also plays optimally


# Since the opponent is playing optimally, he will try to minimize the player’s points, i.e.,
#  the opponent will make a choice that will leave the player with minimum coins
def findMaxCoins(coin, i, j, lookup):
 
    # base case: one pot left, only one choice possible
    if i == j:
        return coin[i]
 
    # if we are left with only two pots, choose one with maximum coins
    if i + 1 == j:
        return max(coin[i], coin[j])
 
    # if the subproblem is seen for the first time, solve it and
    # store its result in a lookup table
    if lookup[i][j] == 0:
        # if the player chooses front pot `i`, the opponent is left to choose
        # from [i+1, j].
        # 1. If the opponent chooses front pot `i+1`, recur for [i+2, j]
        # 2. If the opponent chooses rear pot `j`, recur for [i+1, j-1]
 
        start = coin[i] + min(findMaxCoins(coin, i + 2, j, lookup),
                            findMaxCoins(coin, i + 1, j - 1, lookup)) # Since the opponent is playing optimally, he will try to minimize the player’s points, i.e.,
#  the opponent will make a choice that will leave the player with minimum coins

        # if a player chooses rear pot `j`, the opponent is left to choose
        # from [i, j-1].
        # 1. If the opponent chooses front pot `i`, recur for [i+1, j-1]
        # 2. If the opponent chooses rear pot `j-1`, recur for [i, j-2]
 
        end = coin[j] + min(findMaxCoins(coin, i + 1, j - 1, lookup),
                            findMaxCoins(coin, i, j - 2, lookup)) # Since the opponent is playing optimally, he will try to minimize the player’s points, i.e.,
#  the opponent will make a choice that will leave the player with minimum coins
 
        # assign a maximum of two choices
        lookup[i][j] = max(start, end)
 
    # return the subproblem solution from the dictionary
    return lookup[i][j]
 
 
if __name__ == '__main__':
 
    # pots of gold arranged in a line
    coin = [4, 6, 2, 3]
 
    # Create a table to store solutions to subproblems
    lookup = [[0 for x in range(len(coin))] for y in range(len(coin))]
 
    print('The maximum coins collected by player is',
        findMaxCoins(coin, 0, len(coin) - 1, lookup))
