import statistics

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        hash_ = collections.defaultdict(list)
        for item in items:
            hash_[item[0]].append(item[1])
        
        ans = []
        for key, value in hash_.items():
            scores = sorted(value)[-5:]
            avg = int(statistics.mean(scores))
            ans.append([key, avg])
            
        return ans
            
