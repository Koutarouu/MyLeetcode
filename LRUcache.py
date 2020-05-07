class LRUCache: 
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.curops = 0

    def get(self, key: int) -> int: #O(1)
        if key in self.cache:
            x = self.cache[key]
            x[1] = self.curops
            self.curops+=1
            return x[0]
        return -1

    def put(self, key: int, value: int) -> None: # O(Capacity)
        if key in self.cache or len(self.cache) < self.capacity:
            self.cache[key] = [value, self.curops]
        else: #if len(self.cache) == self.capacity:
            minv = 1e9-5
            mink = 0
            for k, v in self.cache.items():
                if v[1] < minv:
                    minv = v[1]
                    mink = k
            del self.cache[mink]
            self.cache[key] = [value, self.curops]
        self.curops+=1

class LRUCache: #O(1) aprox
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            v = self.cache[key]+0
            del self.cache[key]
            self.cache[key] = v
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
        else:
            del self.cache[next(iter(self.cache))]   #iterator next is like a global pointer here always return the first key of the hash O(1)
            self.cache[key] = value
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)