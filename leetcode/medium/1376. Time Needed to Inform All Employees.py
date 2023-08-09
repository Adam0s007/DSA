# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

# Return the number of minutes needed to inform all the employees about the urgent news.

from typing import List
import collections

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adj[manager[i]].append(i)
        
        q = collections.deque([(headID, 0)])
        res = 0
        while q:
            curr, time = q.popleft()
            res = max(res, time)
            for emp in adj[curr]:
                q.append((emp, time + informTime[curr]))
        return res