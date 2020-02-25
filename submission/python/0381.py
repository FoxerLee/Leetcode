class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = collections.defaultdict(set)
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.m[val].add(len(self.vals))
        self.vals.append(val)
        
        if len(self.m[val]) == 1:
            return True
        else:
            return False
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.m[val]:
            return False
        
        idx = self.m[val].pop()
        last = self.vals[-1]
        
        self.vals[idx] = last
        self.m[last].add(idx)
        self.m[last].discard(len(self.vals)-1)
        
        self.vals.pop()
        
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        idx = random.randint(0, len(self.vals)-1)
        return self.vals[idx]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
