'''
Mental movid
-pick mid
-test predicate
-discard half, repeat
'''
#+sorted array, on answer

'''
FINAL VERSION
'''
def BinarySearch(high, low, sorted_arr, val):
    low = 0
    high = len(sorted_arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if val == sorted_arr[mid]:
            return mid
        elif val > sorted_arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None

#Practice with errors
# c:change
# m:missing
# x:not necessary
# w:wrong logic
def BinarySearch(high, low, sorted_arr, val):
    #x: pos = 0 #track it manually?
    low = 0 #c: sorted_arra[(0)], needs actual position not value at index
    high = len(sorted_arr) - 1 #m: -1, c:sorted_arr[]
    
    while(low<=high):#m:while(low<=high):
     mid = (low + high) // 2 #m:    
     if( val > sorted_arr[mid]):#c: val, mid, low
        #pos = low
        low = mid + 1 #w: low = low + 1
        #some case
     elif(val < sorted_arr[mid]): #c:else 
        #pos = high
        high = mid - 1 #w: high = high - 1 
        # val[i] = val[high]
     if (val == sorted_arr[mid]): #c:
        return mid #c: pos
        
    return None #w: else  

