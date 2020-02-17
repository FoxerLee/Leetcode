class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_dict = collections.defaultdict()
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        paragraph = paragraph.lower().split()
        
        for par in paragraph:
            # par = par.lower()
            if par not in banned:
                if par not in words_dict:
                    words_dict[par] = 1
                else:
                    words_dict[par] = 1 + words_dict[par]
                
        ans = ""
        most = 0
        for word, count in words_dict.items():
            if count > most:
                most = count
                ans = word
        return ans
                
        
