# Czarodziej Pascal ma N stosow porcelanowych talerz, przy czym każdy stos zawiera
# dokładnie k talerzy. Pascal wystawia dziś wieczorem kolację dla P gości i jedzenie
# będzie serwowane na tych właśnie talerzach. Każdy talerz ma pewne piękno określone 
# liczbą całkowitą. Pomóż czarodziejowi wybrać dokładnie P talerzy tak, aby miały one 
# maksymalne możliwe piękno. Ale uwaga! Stos to stos, więc jeśli chcesz zabrać jakis talerz, 
# to musisz też zabrać wszystkie nad nim.

#rozwiazanie:
#f(i,j):
# for l from 1 to k:
# max(f(i-1,j-l) + w[i][l-1], f(i-1,j))
# or
# f(i-1,j)
# i - rozwazany stos
#j - ilosc rozwazanych talerzy


def pascal(M,P): #M - tablica dwuwymiarowa
    dp = {}
    #i - iterator po stosach,j - iterator po konkretnym stosie P - ile wziąć talerzy 
    def dfs(i,j,P):
        if j == len(M[0]) and i +1 < len(M): #sytuacja w ktorej inkrementowalismy j zakladajac ze wzielismy wczesniejszy element
            # ale wychodzimy poza tablice - musimy przejsc do nastepnej kolumny jesli sie da!
            j = 0
            i +=1
        if P != 0 and i >= len(M) or j >= len(M[0]): return False,0
        elif P == 0:  return True,0 
        if (i,j,P) in dp: return True,dp[(i,j,P)]
        cost = 0

        ans2 = dfs(i,j+1,P-1)
        if ans2[0]:
            cost = max(cost, M[i][j]+ ans2[1])
        ans1 = dfs(i+1,0,P)
        if ans1[0]:
            cost = max(cost,ans1[1])
            
        #albo juz omijamy element z obecnego stosu i idziemy do nastepnego, albo
                    #bierzemy obecny element ze stosu i iterujemy w dol 
        dp[(i,j,P)] = cost 
        return True,dp[(i,j,P)]
    
    return dfs(0,0,P)[1]
M = [[1,2,7],
    [3,4,2],
    [1,1,5]
    ]

P = 3
print(pascal(M,P))




