from zad10ktesty import runtests

def answer(iteracje):
    ans = []
    def rek(index):
        i,value = index
        if i != -1:
            rek(iteracje[i])
            ans.append(value)
    rek(iteracje[-1])
    return ans


def dywany ( N ):
    dp = [N]*(N+1)
    iteracje = [[-1,0]]*(N+1)
    dp[0] = 0
    for target in range(1,N+1):
        for s in range(1,target+1):
            square = s*s
            if target - square < 0:
                break
            if dp[target] >  1+dp[target-square]:
                dp[target] = 1 + dp[target-square]
                iteracje[target] = [target - square,s] #[index,value]
    
    return answer(iteracje)  #Tutaj proszę wpisać własną implementację


runtests( dywany )

