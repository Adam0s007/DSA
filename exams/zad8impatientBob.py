# Niecierpliwy Bob ma wykonać k spośród prac J1...Jn, gdzie każda praca jest opisana 
# przez czas rozpoczęcia oraz czas zakończenia:
# struct Job {
#     int start,end; //czas rozpoczęcia i zakończenia (wyrażone w minutach)
# };
# Bob może wybrać dowolne k prac, byle w jednej chwili nie musiał zajmować się więcej niż jedną.
# Bob jest niecierpliwy i chce zminimalizować sumę czasu, jaki czeka między wybranymi pracami.
# Proszę zaimplementować funkcję:
#     int impatientBob(Job J[], int n, int k);
# która na wejście otrzymuje tablicę n prac (posortowanych rosnąco ze względu na czas zakończenia)
# i liczbę k, a zwraca minimalną sumę minut, które musi czekać Bob między pracami (lub -1 jeśli nie da się
# wybrać k niepokrywających się zadań). Proszę skrótowo opisać wykorzystany algorytm.

#Bob jest niecierpliwy i chce wykonać k prac, ale tak, żeby zminimalizować czas przerwy pomiędzy pracami.

def niecierpliwy_bob(job, k):
    dp = [[[10**9, -1] for _ in range (len(job))] for _ in range (k+1)] #przechowujemy ilość zmarnowanego czasu i kiedy skończyliśmy tę pracę
    # dp[k][Jobs][]
    for i in range (len(job)):  # dp[k][Jobs][]
        # if i <= k:
        #     dp[i][0][0] = 0
        #     dp[i][0][1] = job[0][1]
        dp[0][i][0] = 0
        dp[0][i][1] = 0
        dp[1][i][0] = 0
        dp[1][i][1] = job[i][1]

    def f(k, i): #nasze aktualne k , nasza i-ta praca!
        if dp[k][i] != [10**9, -1]:
            return dp[k][i]
        for p in range (0, i): #rozpatrujemy  wszystkie prace do i-tej bez niej
            if job[i][0] >= dp[k-1][p][1]: #mogę wykonać tę pracę
                if dp[k][i][0] > dp[k-1][p][0] + (job[i][0] - dp[k-1][p][1]):
                   dp[k][i][0] = dp[k-1][p][0] + (job[i][0] - dp[k-1][p][1])
                   dp[k][i][1] = job[i][1]

    for i in range (1, k+1):
        for j in range (len(job)):
            f(i, j)
    print(dp[k][len(job)-1][0]) #jesli to inf to zwroc -1

k = 4
job = [(1,4),(2,4),(4,5),(4,6),(7,9),(8,10),(12,15),(11,16)] # (start,koniec)
niecierpliwy_bob(job, k)
        
