'''
Mental Movie(Dynamic Programming using 0/1 knapsack)
-DP over items and weight capacity.
'''
#Practice with errors
# c:change
# m:missing
# x:not necessary
# w:wrong logic

#Memoize a recursive solution
def dp():
    # create a dp[n+1] initialized to -1
    for _ in range(0,len(dp[n])):
    dp[n+1] = -1

    #check for solution if solution is already computed in dp flag array
    if(dp[n] != -1 ):
        return dp[n]

    else:
        dp[n] = soln

    
