from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None


def knapsnackProblem(first):
  B = None
  if first: B = first.fundusze
  else: return 0 #brak glosow jesli okregu nie ma

  P = [] #glosy
  W = [] #oplaty
  while first:
    P.append(first.wyborcy)
    W.append(first.koszt)
    first = first.next

  #teraz wlasciwy problem plecakowy
  dp = [[0 for i in range(B+1)] for j in range(len(P))]
  for i in range(B+1): #rozpatrywany 1. glos
    if i >= W[0]: dp[0][i] = P[0] #mozemy to oplacic gdy mamy pewną ilosc pieniedzy

  for i in range(1,len(dp)):
    for j in range(B+1):
      dp[i][j] = dp[i-1][j] #albo nie bierzemy pod uwage nowych glosow
      if j >= W[i]: dp[i][j] = max(dp[i][j], P[i] + dp[i-1][j-W[i]]) 
      #dp[i-1][j]  -> nie bierzemy nowych glosow ( nie ponosimy nowych kosztow) zostaje to co bylo przy rozpatrywaniu wczesniejszych glosow
      #dp[i-1][j-W[i]] + P[i] -> bierzemy nowy glos (ponosimy koszt W[i]) i bierzemy P[i] glosow
  return dp[-1][-1]

      





def wybory(T):
    maks_glosy = 0
    for head in T:
      maks_glosy += knapsnackProblem(head)
    
    return maks_glosy

runtests(wybory, all_tests = True)