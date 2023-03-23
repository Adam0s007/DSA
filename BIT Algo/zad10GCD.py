# Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n]. 
# Proszę napisać algorytm znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich 
# GCD jest różny od 1. Algorytm powinien działać jak najszybciej



#rozwiazanie: O(n * pierw z n)
#pamietaj ze to nie musza byc podzbiory spojne!
#najlepiej zrobic pierw z n bucketow, (podz przez 2, podz przez 3 itd. do pierw. z n)

#kazda liczba bedzie zapisana do tych bucketow, w ktorych sie dzieli (bucketow jest pierw z n -1)
import math

def GCD_pozdzbior(tab):
    n =  len(tab)
    pierw_n = math.floor(math.sqrt(n))
    buckets = [[] for _ in range(pierw_n-1)]
    for elem in tab:
        for i in range(2,pierw_n+1):
            if elem % i ==0:
                buckets[i-2].append(elem) 
    maksim = 0
    #printing:
    for i in range(len(buckets)):
        print(buckets[i])
    for i in range(len(buckets)-1,-1,-1): #idziemy od tylu aby GCD bylo mozliwie najwieksze jesli mamy te same rozmiary przy roznych GCD
        if maksim < len(buckets[i]):
            maksim = len(buckets[i])
    return maksim

tab = [9,5,3,2,5,6,8,7,5,10]
print(GCD_pozdzbior(tab))