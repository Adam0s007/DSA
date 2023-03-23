from egzP5atesty import runtests 
#rozwiazanie Szymona:
# def inwestor ( T ):
#     s = [-1,0]
#     n = len(T)
#     area = 0
#     i =0
#     LS = [-1 for i in range(n)]
#     RS = [n for _ in range(n)]

#     for i in range(1,n):
#         while s[-1] != -1 and T[s[-1]] > T[i]:
#             RS[s[-1]] = i #a boundary to a value which is on our stach
#             s.pop()
#         if T[i] == T[i-1]:
#             LS[i] = LS[i-1]
#         else:
#             LS[i] = s[-1]
#         s.append(i)
    
#     for j in range(n):
#         area = max(area,T[j]*(RS[j] - LS[j] - 1)) #we are computing without boundaries
#     return area

#rozwiazanie neetCode: (szybsze O(n))
def inwestor(heights):
    maxArea = 0
    stack = [] #pair: (index,height)
    for i,h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea,height*(i-index))
            start = index
        stack.append((start,h))
    #wszystko co zostalo na stosie oznacza, że można wykalkulować pole od pozycji "i" do konca tablicy o wysokosci "h"  
    for i,h in stack:
        maxArea = max(maxArea,h*(len(heights) - i))
    return maxArea

runtests ( inwestor, all_tests=True )