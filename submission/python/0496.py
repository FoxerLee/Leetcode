class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        pairs = collections.defaultdict(int)
        for num in nums2:
            while stack != [] and num > stack[-1]:
                tmp = stack.pop(-1)
                pairs[tmp] = num
                
            stack.append(num)
            
        while stack != []:
            tmp = stack.pop()
            pairs[tmp] = -1
            
        res = []
        for num in nums1:
            res.append(pairs[num])
            
        return res
