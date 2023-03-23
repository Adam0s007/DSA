# Zaproponuj klase reprezentujaca strukture danych, ktora w konstruktorze
# dostaje tablice liczb naturalnych dlugosci n o zakresie wartosci [0,k]. 
# Ma ona zwracac informację o tym, ile liczb w zakresie [a,b] bylo w tabilcy
# ma dzialac w czasie O(1). Mozna zalozyc, ze zawsze a>=1, b <=k

class tablica:
    def __init__(self,tab):
        self.tab = tab
        self.n = len(tab)
        self.k = max(tab)
        self.C  = [0 for i in range(0,self.k+1)]
        for i in range(self.n):
            self.C[self.tab[i]] +=1
        print(self.C)
        for i in range(1,self.k+1):
            self.C[i] += self.C[i-1]
        print(self.C)
    
    def count_num_in_range(self,a,b):
        if a < 1 or b > self.k: return 0
        return self.C[b] - self.C[a-1]


tab = [1,7,9,7,4,2,1,3,4,5,6,8,8,5,3,22,4,5,3,4]

obiekt = tablica(tab)
print(obiekt.count_num_in_range(9,22))
arr = tab
arr.sort()
print(arr)

