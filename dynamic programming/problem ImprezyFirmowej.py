# Impreza jest dopuszczalna jeśli dla żadnego zaproszonego pracownika nie zaprosiliśmy jego 
# bezpośredniego przełożonego
# wartością imprezy jest suma współczynników fun zaproszonych
# zadanie: znaleźć wartość najleprzej dopuszczalnej imprezy

class Employee:
    def __init__(self,fun):
        self.fun = fun
        self.emp = [] #tablica dzieci węzła
        self.f = -1
        self.g = -1

# f(v) - gdzie v to węzeł drzewa -> wartość najlepszej imprezy poddrzewa zakorzenionego w v (samo v może być ale nie musi)
# g(v) -> j. wyżej pod warunkiem, że v nie idzie na imprezę

# g(u) = {suma po wszystkich v - pracownik(u)} <=> Ef(v)
# f(u) = max(g(u), fun(u) + Eg(v)) <=> gdy u nie idzie na impreze to g(u), gdy u idzie to jego fun(u) + pracownicy jego pracownikow! -> Eg(v)
# bo bezposredni pracownik nie może


def g(u):
    if u.g != -1:
        return u.g
    u.g = 0
    for v in u.emp:
        u.g += f(v)
    return u.g 

def f(u):
    if u.f != -1: return u.f
    f1 = g(u)
    f2 = u.fun

    for v in u.emp:
        f2 += g(v)
    u.f = max(f1,f2)
    return u.f


 