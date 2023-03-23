from zad6ktesty import runtests 

def haslo ( S ):
    if not S: return 0
    if S[0] == "0": return 0
    dp = [0 for x in range(len(S) + 1)] 

        # base case initialization
    dp[0] = 1 
    dp[1] = 1   #(1)
    for i in range(2, len(S) + 1): 
        # One step jump
        if 0 < int(S[i-1:i]) <= 9:    #(2)
            dp[i] += dp[i - 1] #one way to write code
        # Two step jump
        if 10 <= int(S[i-2:i]) <= 26: #(3)
            dp[i] += dp[i - 2] #sec way to write code
    return dp[len(S)]

runtests ( haslo )