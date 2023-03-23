from egzP4btesty import runtests 

class Node:
  def __init__(self, val, parent):
    self.left = None
    self.right = None
    self.parent = parent
    self.key = val
    self.x = None #dam tablicę [poprzednik, następnik]


def sol(root, T):
  
  def find_minimum(root1):
    while root1.left != None:
        root1=root1.left
    return root1

  def find_maximum(root1):
      while root1.right != None:
          root1 = root1.right
      return root1

  def successor(x): #następnik
    if x.right != None:
        return find_minimum(x.right)

    y = x.parent
    while y != None and x == y.right: #dopóki rodzic nie jest Nonem i x jest cały czas prawym dzieckiem, idę w górę drzewka
        x = x.parent
        y = y.parent #x.parent.parent
    return y


  def predecessor(x): #poprzednik
      if x.left != None:
          return find_maximum(x.left)
      
      y=x.parent
      while y != None and x == y.left:
          x = x.parent
          y = y.parent
      return y


  ans = 0
  for i in range (len(T)):
    prec = predecessor(T[i])
    suc = successor(T[i])
    if T[i].key == (prec.key + suc.key) / 2:
      ans += T[i].key
  
  return ans

w11 = Node(11, None)
w5 = Node(5, w11)
w11.left = w5
w15 = Node(15, w11)
w11.right = w15
w3 = Node(3, w5)
w5.left = w3
w8 = Node(8, w5)
w5.right = w8
w12 = Node(12, w15)
w15.left = w12
w7 = Node(7, w8)
w8.left = w7
w10 = Node(10, w8)
w8.right = w10
T = [ w5, w7, w8, w11, w12 ]

#print(sol(w11, T))   
runtests(sol, all_tests = True)