from typing import List
import random

class Solution:

    def __init__(self, w: List[int]):
        self.helperValues = []# should be a list of indices [0, 1, 1, 1] => 0 is picked with 25% prob and 1 is picked with 75% prob if we use random. randint()
        wSum = sum(w)
        for i,w in enumerate(w):
            prob = (w/wSum)
            count = round(1e5*prob)
            self.helperValues.extend([i]*count)
        
    def pickIndex(self) -> int:
        rnd = random.randrange(0, len(self.helperValues))
        return self.helperValues[rnd]

# Your Solution object will be instantiated and called as such: