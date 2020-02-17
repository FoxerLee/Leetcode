class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        word_len = len(beginWord)
        
        helper_list = collections.defaultdict(list)
        visited = []
        for word in wordList:
            for i in range(word_len):
                helper_list[word[:i]+'-'+word[i+1:]].append(word)
                
        visited.append(beginWord)
        
        queue = collections.deque([(beginWord, 1)])
        while queue:
            word, steps = queue.popleft()
            for i in range(word_len):
                # helper_word = word[:i]+'-'+word[i:]
                for w in helper_list[word[:i]+'-'+word[i+1:]]:
                    if w == endWord:
                        return steps + 1
                    elif w not in visited:
                        visited.append(w)
                        queue.append((w, steps+1))
                # helper_list[word[:i]+'-'+word[i+1:]] = [] 
        return 0
            
        
