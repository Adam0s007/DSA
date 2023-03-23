# Dostajemy na wejsciu 3 stringi: A,B,C. A i B są tej samej dlugosci. Zachodzą następujące 
# wlasciwosci:
# 1) Litery na tym samym indeksie w stringach A i B są rownowazne. 
# 2) Jezeli litera a jest rownowazna z literą b, to litera b jest z rownowazna 
# z literą a. 
# 3) Jezeli litera a jest rownowazna z b, a litera b z literą c, to 
# litera a jest rownowazna z literą c. 
# 4) Kazda litera jest rownowazna sama ze sobą. 

# W stringu C mozemy zamieniac dowolną literę z literą do niej rownoważną. 
# Jaki jest najmniejszy leksykograficznie string, ktory mozemy w tej sposob skonstruować?

class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value


def make(x):
    return Node(x)


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if x.value < y.value: y.parent = x
    else: 
        x.parent = y

def rownowazne(A,B,C):
    
    count_chars = ord('z') - ord('a') + 1
    visited = [False for i in range(count_chars)]
    sets = [make(chr(ord('a')+i)) for i in range(count_chars)] #dla wszystkich liter od a do z
    
    for i in range(len(B)):
        znB = ord(B[i]) - ord('a')
        visited[znB] = True
        znA = ord(A[i]) - ord('a')
        visited[znA] = True
        if find(sets[znA]) != find(sets[znB]): 
            union(sets[znA],sets[znB])
    
    #zamieniamy wszystkie litery z c z literami rownowaznymi!
    ans = ['' for i in range(len(C))]
    for i in range(len(C)):
        znC = ord(C[i]) - ord('a')
        ans[i] = str(find(sets[znC]).parent.value)
    
    return "".join(ans)


print(rownowazne("tgfcvv","amoait","natali"))
