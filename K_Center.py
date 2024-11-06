# D data, M centers, minimize the maximum distance between a data point and its nearest center
def min_max_distance(arr, M):
    arr.sort()  # Sort positions to enable binary search

    # D=1 [1,2,8,10], M=2 should resturn false but return true
    #stop1=1, count=1
    #pos8-stop1>1, so left_pos=8
    #pos10-left_pos>1, so stop2=8, count=2
    #pos10-stop2>1, so left_pos=10
    def can_place_stops_with_distance(D):
        start_idx=0
        #Place the first stop at the farthest place where the first stop can be placed
        while start_idx<len(arr) and abs(arr[start_idx]-arr[0])<=D:
            start_idx+=1
        if start_idx==len(arr):
            count=1
            if count<=M:
                return True
            else:
                return False

        # place the first stop
        #arr[start_idx]-arr[0]>D
        #arr[start_idx-1]-arr[0]<=D
        start_idx-=1
        last_stop=arr[start_idx]
        count=1

        left_pos = 0  # the farthest left position the next stop can reach, 0 has no meaning
        left_pos_set = True  # True: can set left_pos, False: cannot set left_pos

        #place the following stops
        for idx,pos in enumerate(arr[start_idx+1:],start=start_idx+1):
            # skip positions that can be reached by last stop
            if abs(pos-last_stop)<=D:
                continue
            #abs(pos-last_stop)>D
            #the first position can't be reached by last stop
            if left_pos_set:
                left_pos=pos
                left_pos_set=False

            #place next stop at (farthest position that can reach left_pos) OR current position is the last position
            if (idx+1<len(arr) and abs(arr[idx+1]-left_pos)>D) or idx==len(arr)-1:
                last_stop=pos
                count+=1
                left_pos_set=True #can reset left_pos_set
                if count>M:
                    break
        else:
            return True #once feasible, return True
        return False #no feasible solutions


    # Binary search for the minimum "maximum distance" D
    left, right = 0, arr[-1] - arr[0]
    while left < right:
        mid = (left + right) // 2
        if can_place_stops_with_distance(mid):
            right = mid  # Try a smaller distance
            #why not right=mid-1? because mid is feasible
        else:
            #why not left=mid? because mid is not feasible
            left = mid + 1  # Increase distance to make placement feasible

    return left  # The minimum feasible "maximum distance"

# Example usage
arr = [1, 2, 8, 10]
M = 2
print(min_max_distance(arr, M))  # This will output the minimized max distance






