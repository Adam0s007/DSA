# Dostajemy listę wartości. Gramy z drugim graczem. Wybieramy zawsze jedną
# wartość z jednego z końców tablicy i dodajemy do swojej sumy, a następnie 
# to samo robi nasz przeciwnik. Zakładając, że przeciwnik gra optymalnie, jaką
# maksymalną sumę możemy uzbierać?
# "Uogólniony problem paczki mentosów"

# f(i,j) = max(A[i] + min(f(i+2,j),f(i+1,j-1)),A[j] + min(f(i+1,j-1),f(i,j-2)))
# 