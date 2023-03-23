from egz1atesty import runtests

def snow( S ):
    ans = 0
    i = 0
    S.sort(reverse=True)
    while i < len(S) and S[i] - i > 0:
        ans += S[i] - i
        i+=1
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
