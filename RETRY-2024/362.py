from collections import deque


class HitCounter:

    def __init__(self):
        self.dq = deque()


    """
    @param timestamp: the timestamp
    @return: nothing
    """
    def hit(self, timestamp: int):
        self.dq.append(timestamp)

    """
    @param timestamp: the timestamp
    @return: the count of hits in recent 300 seconds
    """
    def get_hits(self, timestamp: int) -> int:
        earliest_ok_timestamp = timestamp - 300
        
        while self.dq and self.dq[0]<=earliest_ok_timestamp:
            self.dq.popleft()
        
        return len(self.dq)