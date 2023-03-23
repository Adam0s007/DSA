# mamy dana tablice stringow, gdzie suma dl wszystkich stringow jest rowna n.
# Napisz algorytm ktory posortuje tę tablicę w czasie o(n).
# Mozna zalozyc, ze stringi skladają się wylacznie z malych liter alfabetu lacinskiego.

def bucketSort(tab,n):
    maks = 0

    for i in range(tab):
        maks = max(len(tab[i]),maks)
    bucket = [[] for i in range(n)]

tab = ["ala","ma","kota","dom","stacja","Ukraina","Polska","USA"]
print(len("ala"))