
# Mamy dany ciąg napisów (słów) S = [s1,...,sn] oraz pewien napis t. Wiadomo,
# że t można zapisać jako złączenie pewnej ilości napisów z S( z powtórzeniami). 
# Na przykład dla S = [s1,s2,s3,s4,s5] gdzie s1 = ab, s2 = abab, s3 = ba,
# s4 = bab, s5 = b, napis t = ababbab mozna zapisac, miedzy innymi jako s2s4 lub 
# jako s1s1s3s5. Taki wybor konkretnych si nazywamy reprezentacją. Przez szerokosc
# reprezentacji rozumiemy dlugosc najkrotszego si nalezacego do reprezentacji -
# dla s2s4 szerokosc to 4, a dla s1s1s3s5 szerokosc to 1. 
# Zaimplementuj algorytm, ktory majac na wejsciu S oraz t znajdzie maksymalną szerokosc reprezentacji t
# (tzn. najkrotszy napis w jej reprezentacji jest najdluzszy) . Oszacuj czas dzialania algorytmu.




def max_width(t,s):
    dp = {}
    #i - iterator w tablicy s
    #m - ilosc wykorzystanych napisow
    #niech poczatkowo i == 0 zeby k bylo rowne 0
    def dfs(i,arr,m):
        if i >  len(t):  return False, 0
        if i == len(t):  return True, min(arr) #zwraca najmniejszy napis
        if (i,m) in dp: return True,dp[(i,m)]
       
        currMinim = 0
        for k in range(len(s)): # k iterowany przez całą tablicę arr
            if len(s[k]) + i <= len(t) and s[k] == t[i:i+len(s[k])]: #jesli dany napis z s pasuje do napisu w t 
                daSie, value = dfs(i+len(s[k]),[*arr,len(s[k])],m+1)
                if daSie == True:
                    currMinim = max(currMinim, value)
        
        dp[(i,m)] = currMinim 
        return True,currMinim

    return dfs(0,[],0)[1]

s = ["ab","abab","ba","bab","b"]
t = "ababbab"
print(max_width(t,s))
t = "abbaabba"
print(max_width(t,s))
s = ["ad","am","ada","m","adam"]
t = "adam"
print(max_width(t,s))






