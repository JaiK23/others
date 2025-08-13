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
def dp_kp(n,w): #m:
    #2) Base case: if w ==0 or n == 0, return 0.(Guard agains negative index)
    if (w <= 0 or n <= 0): #c: ||, #c: w == 0/n== 0
        return 0
                

    #3 check for solution if solution is already computed in dp flag array
    if(dp[n][w] != -1 ): #c: dp[n] != -1 , #c: dp[n][w] = -1
        return dp[n][w]  #c: dp[n]


    #0)additional boundary checking

    #Guard Against Negative Capacity :m
    if(weight[n-1] > w):
        dp[n][w] = dp_kp(n-1, w)
        return dp[n][w] #m:
    #4) Finally run dp
    else:
                    #Not taking item n  and     taking item
        dp[n][w] = max( dp_kp(n-1,w)          , value[n-1] + dp_kp(n-1, w-weight[n-1]) ) #m:, #c:[n], #c:dp(), #c:value[n]/weight[n]
        return dp[n][w] #m:
#Setup variables
# value = [12, 34, 82]
# weight = [2, 10, 3]
# n = 3
# w = 2

# value = [10]
# weight = [2]
# n = 1
# w = 2
# # Expected Output: 10

value = [10]
weight = [5]
n = 1
w = 2
# Expected Output: 0


#1) create a dp initialized to -1, over w+1 and n+1
dp = [ [-1 for _ in range(w+1)]for _ in range(n+1)]#w: for _ in range(0,len(dp[n])): , #w: dp[n][w]=[-1*[for _ in range(dp[n][w]], #c: -1*
                                                        #w: dp[n+1] = -1  

print("Dp with knapsack is:", dp_kp(n,w))

    
