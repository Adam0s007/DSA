from egzP1atesty import runtests 



def titanic( W, M, D ):
    iter = 0
    possible = []
    for i in range(len(M)):
        if i == D[iter]:
            possible.append(M[i][1])
            iter+=1
            if iter == len(D):break
    
    fromLetterToCode = {}
    for letter,code in M:
        fromLetterToCode[letter] = code
    code = ""
    for znak in W:
        code += fromLetterToCode[znak]
    
    # dp = [float("inf") for i in range(len(code)+1)]
    # dp[len(code)] = 0

    # for i in range(len(dp)-2,-1,-1):
    #     for elem in possible:
    #         if i + len(elem) <= len(dp) and elem == code[i:i+len(elem)]:
    #             dp[i] = min(dp[i],1+ dp[i+len(elem)])
    # return dp[0]

    DICT = {}




runtests ( titanic, recursion=False )