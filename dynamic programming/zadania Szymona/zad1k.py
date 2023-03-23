from zad1ktesty import runtests

def roznica( S ):
    if "0" not in S: return -1
    dp = [[0,0] for i in range(len(S))] #[[zeros,ones] ...] zlicza ile jest tych liczb
    dp[0][0] = 1 if S[0] == "0" else 0
    dp[0][1] = 1 if S[0] == "1" else 0
    ans = 0
    ones = 0
    zeros = 0
    for i in range(1,len(S)):
        if S[i] == "0": 
            dp[i][0] = 1+ dp[i-1][0]
            dp[i][1] = dp[i-1][1]
        else: 
            dp[i][1] = 1 + dp[i-1][1]
            dp[i][0] = dp[i-1][0]
    for a in range(len(S)):
        for b in range(a+1,len(S)):
            ones = abs(dp[b][1] - dp[a][1])
            zeros = abs(dp[b][0] - dp[a][0])
            ans = max(ans,zeros - ones)
    return ans


runtests ( roznica )