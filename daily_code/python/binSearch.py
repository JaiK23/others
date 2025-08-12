'''
Mental movid
-pick mid
-test predicate
-discard half, repeat
'''
#+sorted array, on answer
def BinarySearch(high, low, sorted_arr, val):
    pos = 0
    low = sorted_arra(0)
    high = sorted_arr([len(sorted_arr)])
    mid = (low + high) / 2
    if( val > sorted_arr[low]):
        pos = low
        low = low + 1
        #some case
    else:
        pos = high
        high = high - 1 
        # val[i] = val[high]
    if (val == sorted_arr[pos]):
        return pos

