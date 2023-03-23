# Na tablicach w kantorze wisi lista trójek (waluta1,waluta2,kurs).
# Każda z takich trójek oznacza, że kantor kupi n waluty2 za kurs*n waluty1. 

# 1) znajdź najkorzystniejszą sekwencję wymiany waluty A na walutę B. 
# 2) Czy istnieje taka sekwencja wymiany walut, ktora zaczyna sie i konczy sie w tej samej walucie
# i konczymy z większą ilością pieniędzy niż zaczynaliśmy?


#rozwiazanie:
#  wierzcholkami bedą waluty, kursami bedą krawedzie
# uzywamy algorytmu bellmana forda, zobacz jedną rzecz. przy relaksacji tym razem musielibysmy
# stosować mnożenie zamiast dodawania! to by moglo doprowadzic do nieskonczonych cykli!
# kursy bedace wagami krawedzi zamieniamy na logkurs gdzie kurs to waga krawedzi
#robimy to z dwoch powodow:
# relaxacja bedzie dodawaniem a nie mnożeniem, oraz logk gdzie k e (0,1) bedzie ujemny (a to pokrywa sie z 
# faktem, ze przy mnozeniu liczb e (0,1) zmniejszają się.), a logk, gdzie k >1 bedzie dodatni!
# poza tym funkcja log (logarytm dziesietny) jest monotoniczna rosnaca wiec wszystkie dzialania pokrywają się 
# tzn tam gdzie mialo byc mniej bedzie mniej, a tam gdzie wiecej to bedzie wiecej

# tak naprawde wagi krawedzi, czyli nasze kursy musimy jeszcze po zamianie na logk przemnozyc przez minus.
# bellam ford szukal najkrotszych sciezek, a my musimy znalezc jak najkorzystniesze przejscia z walut, czyli
# jesli sie da,to zeby zarobic JAK NAJWIECEJ, wiec aby dzialal klasyczny bellam ford musimy przemnożyć przez -1
# k -> -logk , gdzie  k - waga krawedzi ozn kurs


#jesli znajdziemy wtedy cykl ujemny, to oznacza ze istnieje sekwencja wymiany walut, ktora konczy sie 
# w tej samej walucie a my bedziemy posiadac wiecej pieniedzy, 

# algorytm zalatwia od razu oba podpunkty

#wtedy kursy mniejsze od 1 bedą dodatnie
# kursy wieksze od 1 bedą ujemne
    
        
