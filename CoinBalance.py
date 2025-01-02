"""
given some coins as in a set with element like [value, count], check if target chould be matched with the coins.
coins: [[1, 4], [2, 4], [5, 3], [10, 2]]
target: 39
"""

# def coin_change(coins, target):
#     def backtrack(coins,target, )
#     return True


from collections import defaultdict

def coin_change(coins, target)->bool: #coins 2D are, in target
    total_selection=0 #total selection of all coins
    #corner case
    total_val=0
    for fst_elm,sec_elm in coins:
         total_selection+=sec_elm
         total_val+=fst_elm*sec_elm
    if total_val<target:
         return False
    elif total_val==target:
         return True
    else: #total_val>target
         #flatten coins
         new_coins=[ [ lst_1d[0] ]*lst_1d[1] for lst_1d in coins]
         new_coins=[ elm  for lst_2d in new_coins for elm in lst_2d   ]
         #cur_sel=0 is judging the 1st selection, cur_sel=1, has finished 1st selection,
         #memo[cur_sel][cur_val]
         memo=defaultdict(lambda: defaultdict(lambda: True))   #initialize 2D dict
         def backtrack(new_coins,target, cur_sel, cur_sum, memo)->bool:
	     #pre
                 if cur_sum==target:
                       return True

                 if cur_sel==total_selection:
                       return False

                 if not memo[cur_sel][cur_sum]:
                       return False

	     #in
                 #select the cur_val
                 result=backtrack(new_coins, target, cur_sel+1, cur_sum+new_coins[cur_sel],memo)
                 if result:
                         return True
                 #don’t select the cur_val
                 result=backtrack(new_coins, target, cur_sel+1, cur_sum,memo)
                 if result:
                         return True

	     #post
                 #current state is a dead end
                 memo[cur_sel][cur_sum]=False
                 return False
         return backtrack(new_coins,target,0,0,memo)
print(coin_change([[1, 4], [2, 4], [5, 3], [10, 2]],39))
#------------------------------------------------------------------------------------
from collections import defaultdict


def coin_change(coins, target) -> bool:
    # Memoization dictionary to store results for (coin index, current sum)
    memo = {}

    def backtrack(index, current_sum):
        # Base cases
        if current_sum == target:  # Target achieved
            return True
        if current_sum > target or index == len(coins):  # Exceeded target or no coins left
            return False
        if (index, current_sum) in memo:  # Already computed this state
            return memo[(index, current_sum)]

        # Current coin value and count
        coin_value, coin_count = coins[index]

        # Try using 0 to `coin_count` of the current coin
        for count in range(coin_count + 1):
            if backtrack(index + 1, current_sum + count * coin_value):
                memo[(index, current_sum)] = True
                return True

        # Mark this state as a dead end
        memo[(index, current_sum)] = False
        return False

    return backtrack(0, 0)


# Example usage
print(coin_change([[1, 4], [2, 4], [5, 3], [10, 2]], 39))  # Output: True
