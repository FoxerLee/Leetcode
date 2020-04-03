class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)
        
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        
        try:
            allstamps = self.dict[key]
            i = bisect.bisect(allstamps, (timestamp, chr(111)))
            return allstamps[i-1][1] if i else ""
        
        except:
            return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
