class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        
        word_len = len(beginWord)
        
        helper_list = collections.defaultdict(list)
        # visited = []
        for word in wordList:
            for i in range(word_len):
                helper_list[word[:i]+'-'+word[i+1:]].append(word)
                
        # visited.append(beginWord)
        
        queue = collections.deque()
        queue.append((beginWord, [beginWord]))
        res = []
        dis = {}
        level = 1
        
        while queue:
            stop = False
            for _ in range(len(queue)):
                word, steps = queue.popleft()
                helper_word = []
                for i in range(word_len):
                    tmp = word[:i]+'-'+word[i+1:]
                    helper_word.extend(helper_list[tmp])
                
                for w in helper_word:
                    if w in dis and dis[w] < level:
                        continue
                    else:
                        dis[w] = level

                    if w == endWord:
                        res.append(steps+[w])
                        stop = True
                    else:
                        queue.append((w, steps+[w]))
            level += 1
            if stop:
                break
                
        return res
        
