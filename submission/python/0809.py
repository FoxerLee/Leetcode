class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        
        s_list, s_v = zip(*[(k, len(list(grp)))  for k, grp in itertools.groupby(S)])

        # print(list(S_list.keys()))
        ans = 0
        for word in words:
            w_list, w_v = zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(word)])
            if w_list != s_list:
                continue
            ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(s_v, w_v))

        return ans

