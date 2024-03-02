class TimeMap:

    def __init__(self):
        self.kvs = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.kvs.keys():
            self.kvs[key] = []
        
        self.kvs[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.kvs.keys():
            return ""
        lst = self.kvs[key]
        
        ret = ""
        
        lft, rgt = 0, len(lst)-1
        
        while lft <= rgt:
            mid = lft + (rgt - lft)//2
            
            
            if lst[mid][0] <= timestamp:
                ret = lst[mid][1]
                lft = mid+1
            else:
                rgt = mid-1
        
        return ret


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)