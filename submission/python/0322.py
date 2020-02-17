class Solution:
    def helper(self, coins, amount, counts):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if counts[amount-1] != 0:
            return counts[amount-1]
        min = 1230914451
        for c in coins:
            res = self.helper(coins, amount-c, counts)
            if res >= 0 and res < min:
                min = res + 1
            counts[amount-1] = -1 if min == 1230914451 else min
        return counts[amount-1]
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        counts = [0 for _ in range(amount)]
        return self.helper(coins, amount, counts)
        
    
