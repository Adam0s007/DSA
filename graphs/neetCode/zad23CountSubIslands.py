# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water)
#  and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). 
# Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 
# that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands.

 

# Example 1:

# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
# Example 2:


# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2 
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        ROWS,COLS = len(grid1), len(grid1[0])
        visit = set()
        
        def dfs(r,c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or \
                grid2[r][c] == 0 or (r,c) in visit:
                return True #edge cased - poniewaz natrafilismy na takie
                # to nie oznacza ze musimy zwracac Falsz! poprostu ten if zwiazany jest
                # z poszukiwaniem calej wyspy
            visit.add((r,c))
            res = True
            if grid1[r][c] == 0: 
                res = False #nie zwracamy od razu! musimy sprawdzić calą wyspę wiec musimy 
                # przejsc przez caly subisland
            res = dfs(r-1,c) and res
            res = dfs(r,c-1) and res 
            res = dfs(r+1,c) and res
            res = dfs(r,c+1) and res
            #wspaniale! odwiedzilismy wszystkie pola zwiazane z wyspą i od razu wskazalismy, czy to moze byc subisland!
            return res             

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid2[r][c] and (r,c) not in visit and dfs(r,c):
                    count +=1
        return count