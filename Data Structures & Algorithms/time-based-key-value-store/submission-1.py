class TimeMap:

    def __init__(self):
        self.key_store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.key_store.get(key):
            self.key_store[key][timestamp] = value

        else:
            self.key_store[key] = {timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        if not self.key_store.get(key):
            return ""

        if self.key_store[key].get(timestamp):
            return self.key_store[key][timestamp]

        ts = list(self.key_store[key].keys())

        l, r = 0, len(ts)-1

        while l<=r:
            mid = (l+r)//2
            
            if ts[mid] < timestamp:
                l = mid+1
            else:
                r = mid-1
        
        if r < 0:
            return ""

        return self.key_store[key][ts[r]]


