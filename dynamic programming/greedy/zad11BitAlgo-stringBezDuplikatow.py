# Dany jest string, w którym niektóre litery się powtarzają. Należy zaproponować 
# algorytm, który usunie ze stringa duplikaty tak, że otrzymany string będzie
# leksykograficznie najmniejszy.

# Przykład: cbacdcbc, odpowiedzią jest acdb.

# Wskazówka: ord("a") = 97; ord("b") = 98; ...; ord('z') = 122.


#rozwiazanie:
# gdy idziemy od przodu do konca tablicy to musimy wszystkie znaki dac do slownika
# jesli znak nie wystepuje w slowniku, to dodajemy go tam i tyle
# jesli natomiast wystepuje juz w slowniku,to:
# jesli ten co juz wystepuje jest > od swojego nastepnika, to nalezy usunac ten znak, w przeciwnym wypadku:
#usuwamy nasz znak



#inny sposob: 
#zliczamy wystepienie kazdej litery
#mozna wykorzystac tez stos 

def remove_duplicats(word):
    word1 = ""
    prev = 0
    word1 += word[prev]
    for i in range(1,len(word)):
        if word[prev] == word[i]:
            continue
        word1 += word[i]
        prev = i
    #usuwanie sytuacji aa...bb..cccc... by bylo samo a....b...c...
    #tworzymy slownik i w nim przechowujemy tylko indeksy
    slownik = {}
    tab = [True for i in range(len(word1))]

    for ind,znak in enumerate(word1):
        if znak not in slownik: slownik[znak] = ind
        else:
            old_ind = slownik.get(znak) #stary indeks, wynajdujemy pierwszy znak w tablicy, ktory ISNIEJE W NASZYM SLOWIE
            i = old_ind + 1
            #tzn jesli juz usunelismy jakies slowo to pod jego indeksem nim w tablicy bedzie False
            # wiec my szukamy pierwszego wystapienia True
            while not tab[i]: i+=1
            if ord(znak) >= ord(word1[i]):
                tab[old_ind] = False
                slownik.pop(znak)
                slownik[znak] = ind #nowy indeks 
            else:
                tab[ind] = False
    strn= ""
    for i in range(len(tab)):
        if tab[i]: strn+=word1[i]
    return strn
        
def remove_duplicats(word):
    stack = []
    count = {}
    for zn in word:
        count[zn] = count.get(zn,0) + 1
    stack.append(word[0])
    verified = {} #nie wiemy co z pierwszą literką

    for znak in word[1:]:
        if ord(stack[-1]) >= ord(znak) and count.get(stack[-1]) > 1:
            count[stack[-1]] =  count.get(stack[-1]) - 1
            stack.pop()
            stack.append(znak)

        elif znak not in verified:
            verified[stack[-1]] = True
            count[znak] =  count.get(znak) - 1
            stack.append(znak)
            verified[znak] = True
            
    
    return "".join(stack)



print(remove_duplicats("cbacdcbc"))
print(remove_duplicats("dcaadccb"))
print(remove_duplicats("abacdcbc"))