class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        
        last_labels = collections.defaultdict()
        
        for i in range(len(S)):
            last_labels[S[i]] = i
            
        ans = []
        
        idx = 0
        while idx < len(S):
            start_idx = idx
            label = S[idx]
            last_idx = last_labels[label]
            
            while idx < last_idx:
                idx += 1
                new_label = S[idx]
                new_last_idx = last_labels[new_label]
                if new_last_idx > last_idx:
                    last_idx = new_last_idx
                    
            ans.append(last_idx-start_idx+1)
            idx += 1
        
        return ans
