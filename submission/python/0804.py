class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        tables = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        for word in words:
            morse = ""
            for char in word:
                morse += tables[ord(char)-ord("a")]
            ans.add(morse)
            
        return len(ans)
