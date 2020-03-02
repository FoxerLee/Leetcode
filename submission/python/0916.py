class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            return count
        
        b_max = [0] * 26
        for b in B:
            for i, c in enumerate(count(b)):
                b_max[i] = max(b_max[i], c)
                
        ans = []
        for a in A:
            # a_count = count(a)
            flag = True
            for i, c in enumerate(count(a)):
                if c < b_max[i]:
                    flag = False
            
            if flag:
                ans.append(a)
                
        return ans
