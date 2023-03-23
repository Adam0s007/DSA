from egz1btesty import runtests
from collections import deque
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.parent = None
    self.x = None     # pole do wykorzystania przez studentow

def wideentall( T ):
    q = deque()
    height = 0
    max_nr_of_leaves = 0
    #bedziemy miec rowniez parentow!
    
    q.append((T,-1))
    bestRow = []
    while q:
      nr_of_leaves = 0
      row = []
      for i in range(len(q)): #ma cala kolejka sie zwolnic na danym poziomie!
        tup = q.popleft()
        node = tup[0]
        parentNode = tup[1]
        node.parent = parentNode
        nr_of_leaves += 1
        row.append(node)
        if node.left: q.append((node.left,node))
        if node.right: q.append((node.right,node))
      
      #wykalkulowanie najlepszego poziomu lisci
      if max_nr_of_leaves < nr_of_leaves:
        max_nr_of_leaves = nr_of_leaves
        bestRow = row.copy()
      elif max_nr_of_leaves == nr_of_leaves:
        bestRow = row.copy()
      height +=1

    #znamy juz poziom z najwiekszą ilością liści który jest najniżej położony
    # znamy parentow kazdego Node,a więc oznaczamy wszystkie Node'y odpowiednio idąc do roota!
    for node in bestRow:
      while node != -1:
        node.x = True
        node = node.parent
    #oznaczone juz mamy, nody na odpowiednich sciezkach! teraz dfs'em wyliczymy do zwrocenia node'y
    counter = [0]

    
    def dfs(node):
      if not node: return
      if node.left and node.right and not node.left.x and not node.right.x:
        counter[0] +=2
        return 
      elif node.left and not node.left.x:
        counter[0] +=1

        dfs(node.right)
      elif node.right and not node.right.x:
        counter[0] +=1
        dfs(node.left)
      else:
        dfs(node.left)
        dfs(node.right)
    dfs(T)
    return counter[0] 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )