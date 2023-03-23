rm = (-1,0,3,3,6,1,4,6,2,5,0,3,5) #reduktor miesiecy
dni = ('niedziela','poniedzialek','wtorek','sroda','czwartek','piatek','sobota')
d = int(input("dzien 1-31   :"))
m = int(input("miesiac 1-12 :"))
r = int(input("rok 1900-2099:"))

#algorytm:
dt = d + rm[m] + (r-1900) + (r-1900)//4
if r % 4 == 0 and m < 3: dt - dt-1 #jesli rok przestepny
dt = dt%7

print(dni[dt])

if __name__=="__main__":
    pass