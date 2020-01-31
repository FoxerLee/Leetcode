class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        pairdic = collections.defaultdict(list)
        
        for p1, p2 in pairs:
            pairdic[p1].append(p2)
            pairdic[p2].append(p1)
            
        for w1, w2 in zip(words1, words2):
            stack = [w1]
            visited = set()
            flag = False
            while stack:
                tmp = stack.pop()
                if tmp == w2:
                    flag = True
                    break
                for nei in pairdic[tmp]:
                    # if nei == w2:
                    #     flag = True
                    #     break
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
            
            if flag == False:
                return False
            
        return True
