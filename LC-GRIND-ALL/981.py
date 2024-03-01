class TimeMap:

    def __init__(self):
        self.kvs = {} # kvs[(key, ts)] = value
        self.kvt = {} # kvt[key] = [ts1, ts2, ts3...]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kvs[(key, timestamp)] = value
        if key not in self.kvt.keys():
            self.kvt[key] = []
        self.kvt[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvt.keys():
            return ""
        def findGoodTime(tsarr, target):
            if not tsarr:
                return -1
            l, r = 0, len(tsarr)-1
            ans = -1
            while l<=r:
                m = (l+r)//2
                if tsarr[m] <= target:
                    ans = tsarr[m]
                    l = m + 1
                else:
                    r = m - 1
            return ans
        
        ts = findGoodTime(self.kvt[key], timestamp)
        
        if ts == -1:
            return ""
        return self.kvs[(key, ts)]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)