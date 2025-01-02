method='dp2' # 'dp' or 'recursion' or 'dp2' or 'dp3'
# dp[x][y] = m
# 当前状态为x个鸡蛋（总共k个鸡蛋），面对 y 层楼(总共n层)
# 这个状态下最少的扔鸡蛋次数为 m
K=10
N=100

if method=='dp': #result=7
    k=K
    n=N

    '''Initialize dp'''
    # dp[x][0]=0 #no floor, no need to check
    # dp[x][1]=1 #one floor, check once
    # dp[0] is dummy row
    dp = [[0, 1] + [float('inf')] * (n - 1) for _ in range(k + 1)]
    for col in range(2, n + 1):
        dp[1][col] = col

    '''transition'''
    for row in range(2, k + 1):
        for col in range(2, n + 1):
            for cur_col in range(1,col+1):
                dp[row][col] = min(
                    dp[row][col],
                    max(
                        dp[row][col - cur_col],  # no break; update in the same row
                        dp[row - 1][cur_col - 1]  # break
                    ) + 1
                )


    print(dp[k][n])

elif method=='recursion':
    def superEggDrop(K: int, N: int):
        memo = dict()

        def dp(K, N) -> int:
            # base case
            if K == 1: return N  # 1 egg, scanning all floors
            if N == 0: return 0  # no floor(no searching space), F must be 0, no need to cast
            # if N==1 is base case, return 1.
            # if break, F must be 0-th floor
            # elif intact, F must be 1-th floor
            # 避免重复计算
            if (K, N) in memo:  # 状态量存元组
                return memo[(K, N)]

            # initiate current result
            res = float('INF')

            # 穷举当前状态所有可能的选择
            for i in range(1, N + 1):  # scanning all floors
                res = min(res,  # min casting
                          max(  # worst situation
                              dp(K, N - i),  # intact
                              dp(K - 1, i - 1)  # break
                          ) + 1  # times+1
                          )
            # 记入备忘录
            memo[(K, N)] = res
            return res

        return dp(K, N)

    print(superEggDrop(K, N))

elif method=='dp2':
    #dp2[k][m]=n  #k eggs, m moves, n is the max floor where F can be identified
    #m must <= N (total floors)

    #base case
    #case1: dp2[0][m]=0, so dp2[0] is dummy row
    #case2: dp2[k][0]=0, 0 moves can't identify any floor
    #case3: dp2[k>=1][1]=1, 1 move can only identify 1st floor
    #case4: dp2[1][m>=1]=m, 1 egg, m moves, can identify m floors (linear scanning)

    #init all 0+ case1 and case2
    dp2=[[0]*(N+1) for _ in range(K+1)]

    #case3:
    for k in range(1,K+1):
        dp2[k][1]=1

    #case4:
    for m in range(1,N+1):
        dp2[1][m]=m

    #transition
    for k in range(2,K+1):
        for m in range(2,N+1):
            dp2[k][m]=dp2[k-1][m-1]+dp2[k][m-1]+1
            if dp2[k][m]>=N: #pruning
                print(m)
                break
elif method=='dp3':
    def superEggDrop(K: int, N: int) -> int:
        # init
        # dp[k][m] = max number of floors that can be tested with k eggs and m moves
        dp = [[0] * (N + 1) for _ in range(K + 1)]

        # why not initialize dp[k>=1][1] and dp[1][m>=1]
        # because they are included in the transition

        m = 0
        # transition
        while dp[K][m] < N:  # outer loop: m (col)
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
        return m


    # Example usage:
    k = 10
    n = 100
    print(superEggDrop(k, n))  # Will print the minimum number of moves needed
