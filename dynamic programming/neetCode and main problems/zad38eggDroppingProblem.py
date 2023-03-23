# A Dynamic Programming based Python Program for the Egg Dropping Puzzle
INT_MAX = 32767
 

 #o((totalFloors^2)*totalEggs)
 
# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(eggs, floors):
    # A 2D table where entry eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(floors + 1)] for x in range(eggs + 1)]
 
    # We need one trial for one floor and 0 trials for 0 floors
    for i in range(1, eggs + 1):
        eggFloor[i][1] = 1 #[eggs][floors]
    #    eggFloor[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, floors + 1):
        eggFloor[1][j] = j

    # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, eggs + 1):
        for j in range(2, floors + 1):
            eggFloor[i][j] = INT_MAX
            for x in range(1, j + 1): #from 1'st floor to j'th floor
                res = 1 + max(eggFloor[i-1][x-1],eggFloor[i][j-x]) #we give max() due to the worst cases! (more trials needed)
                # when we break the egg, so we need to go down or when we don't break an egg, we have j-x floors left
                # and we add 1 to our solution because we need 1 more trial to do these activities!
                eggFloor[i][j] = min(eggFloor[i][j],res)
 
    # eggFloor[eggs][floors] holds the result
    return eggFloor[eggs][floors]
 
# Driver program to test to print printDups
n = 1
k = 12
print("Minimum number of trials in worst case with " + str(n) + " eggs and "
       + str(k) + " floors is " + str(eggDrop(n, k)))
 
# This code is contributed by Bhavya Jain