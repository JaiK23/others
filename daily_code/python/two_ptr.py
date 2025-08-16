'''
When: find element, or find threshold value (min/max) fulfilling condition.
Mental movie: pick mid, test predicate, discard half, repeat.

#Practice with errors
# c:change
# m:missing
# x:not necessary
# w:wrong logic
'''
#Max sub-array

def max_sub_arr(k, arr):
    low = 0
    best= 0 #c:high
    cur = 0 

    for hi in range(len(arr)): #m:
     # if cur > arr[hi]: #c: low, #x: 

     #to iterate elements within the window
        cur += arr[hi]
        while cur > k: #m:, #w: <
            cur = arr[low] ; low = low + 1        #c: ,m:        
        best = max(best, hi-low+1) #c: (arr[cur], arr[hi]) , #m: ""
    #  elif cur < arr[high]:
    #     cur -= high

    return best #c:max(arr[best], arr[cur])
