# Given an integer array, find a contiguous subarray within it that has 
# the largest sum.
#For example: input: [-2,1,-3,4,-1,2,1,-5,4]
#output: Subarray with the largest sum is:
# [4,-1,2,1] with sum 6
def largest(tab):
    l,r = 0,0
    best_l = l
    best_r  = r 
    currSum = 0
    maksimSum = 0
    for i in range(len(tab)):
        currSum += tab[i]
        if currSum < 0:
            currSum = 0
            l = i + 1
            r = l           
        print(l,r)   
        if maksimSum < currSum:
            maksimSum = currSum 
            best_l = l
            best_r = r
        r +=1
    
    #uwaga! moze sie okazac ze tab[best_l:best_r] > tab[best_l:best_r+1]
    return maksimSum,tab[best_l:best_r]

tab  = [-2,1,-3,4,-1,-5,1,-7,8]
print(largest(tab))

        
