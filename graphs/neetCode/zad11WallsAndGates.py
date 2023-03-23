
# You are given a m x n 2D grid initialized with these three possible values.
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 
# to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate.
#  If it is impossible to reach a Gate, that room should remain filled with INF
from collections import deque

from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS,COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()
        
        def addRoom(r,c):
            if ( r < 0 or r == ROWS or c< 0 
            or c == COLS
            or (r,c) in visit or rooms[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])
            

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                rooms[r][c] = dist
                addRoom(r+1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist +=1
