
arr=[1,2,3,101,100]
total=40
#
def findMaxLimit(arr,total):
    #corner case
    if sum(arr)<total:
        return -1
    else:
        #binary search
        limit_left=0
        limit_right=max(arr) #the upper bound of the arr # check

        while limit_left<limit_right:
            limit_mid=(limit_left+limit_right+1)//2
            cur_sum=sum(min(element,limit_mid) for element in arr)
            if cur_sum<=total:
                limit_left=limit_mid
            else:
                limit_right=limit_mid-1
        return limit_left

limit=findMaxLimit(arr,total)
print(limit)