class Solution:
    def addBoldTag(self, s: str, dict: List[str]) -> str:
        def find_all(a_str, sub):
            res = []
            start = 0
            while True:
                start = a_str.find(sub, start)
                if start == -1:
                    break
                res.append([start, start+len(sub)])
                start += 1

            return res


        intervals = []
        for w in dict:
            # intervals += [[m.start(), m.start()+len(w)] for m in re.finditer("(?={0})".format(w), s)]
            intervals += find_all(s, w)

        intervals.sort(key=lambda x: x[0])
        merge = []
        for i in intervals:
            if merge and merge[-1][1] >= i[0]:
                merge[-1][1] = max(merge[-1][1], i[1])
            else:
                merge.append(i)

        offset = 0
        for st,en in merge:
            s = "{0}<b>{1}</b>{2}".format(s[:st+offset],s[st+offset:en+offset],s[en+offset:])
            offset += len("<b></b>")
        return s
            
                
