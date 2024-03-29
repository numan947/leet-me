import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.numsToIdx = {}

    def insert(self, val: int) -> bool:
        if val in self.numsToIdx:
            return False
        
        self.numsToIdx[val] = len(self.nums)
        self.nums.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numsToIdx:
            return False
        idx = self.numsToIdx[val]
        # this ensures O(1) on average
        self.numsToIdx[self.nums[-1]] = idx
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.nums.pop()
        del self.numsToIdx[val]
        return True

    def getRandom(self) -> int:
        pos = random.randrange(0, len(self.nums))
        return self.nums[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()