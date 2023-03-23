# You are given an array points representing integer coordinates of some points on a 2D-plane, 
# where points[i] = [xi, yi].
# The cost of connecting two points [xi, yi] and [xj, yj] 
# is the manhattan distance between them: |xi - xj| + |yi - yj|, 
# where |val| denotes the absolute value of val.
# Return the minimum cost to make all points connected. 
# All points are connected if there is exactly one simple path between any two points.
from queue import PriorityQueue
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        adj = { i:[] for i in range(N) } # i : list of [cost,node]
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        #Prim's
        res = 0
        visit = set()
        minH = PriorityQueue() # [cost,point]
        minH.put((0,0))
        while len(visit) < N:
            cost,i = minH.get()
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    minH.put(neiCost,nei)
        return res

#ten sam kod ale z heapq
import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        adj = { i:[] for i in range(N) } # i : list of [cost,node]
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist,j])
                adj[j].append([dist,i])

        #Prim's
        res = 0
        visit = set()
        # [cost,point]
        minH = [[0,0]]
        while len(visit) < N:
            cost,i = heapq.heappop(minH)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for neiCost,nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minH, [neiCost,nei])
        return res