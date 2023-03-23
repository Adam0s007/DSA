# from tkinter import Y
# from turtle import ycor


# Dany jest ciąg klocków (a1,b1),... (an,bn). Każdy klocek zaczyna 
# się na pozycji ai i ciągnie się do pozycji bi. Klocki mogą
# spadać w kolejności takiej jak w ciągu. Proszę zaimplementować 
# funkcję tower(A), która wybiera możliwie najdłuższy pociąg klocków taki,
# że spadając tworzą wieżę i żadek klocek nie wystaje poza którykolwiek
# z wcześniejszych klocków. Do funkcji przekazujemy tablicę A zawierającą
# pozycje klocków ai,bi. Funkcja powinna zwrócićmaksymalną wysokość wieży
# jaką można uzyskać z klocków w tablicy A.

# Przykład: dla tablicy A = [(1,4),(0,5),(1,5),(2,6),(2,4)] wynikiem jest 3,
# natomiast dla tablicy A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)] wynik  to 2


#rozwiązanie: 
# tworzymy tablicę dp od 0 do n z poczatkowymi wartosicami 1
# wiemy ze ostatni klocek zostal wrzucony najpozniej, wiec idziemy od tylu 
# dla i'tego elementu (idac od najpozniejszego klocka do najwczesniejszego)
#sprawdzamy dp kazdego pozniejszego klocka przy zalozeniu ze klocek pozniejszy zawiera sie w danym i'tym
# robimy: dp[i] = max(dp[i], 1 + dp[j]) dla j e [i+1,len(A))

def zawieraSie(ity,jty):
    return (ity[0] <= jty[0] and ity[1] >= jty[1])

def tower(A):
    dp = [1 for i in range(len(A))]
    for i in range(len(A)-1,-1,-1):
        for j in range(i+1,len(A)):
            if zawieraSie(A[i],A[j]):
                dp[i] = max(dp[i],1 + dp[j])
    return max(dp)


A = [(1,4),(0,5),(1,5),(2,6),(2,4)] 
print(tower(A))
A = [(10,15),(8,14),(1,6),(3,10),(8,11),(6,15)]

print(tower(A))