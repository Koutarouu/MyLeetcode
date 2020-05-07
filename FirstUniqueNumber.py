class FirstUnique:
    def __init__(self, nums: List[int]): #O(nums)
        self.unique = OrderedDict()
        self.visited = {}
        for i in nums:
            if i not in self.visited:
                self.unique[i] = True
            elif i in self.unique::
                del self.unique[i]
            self.visited[i] = True
        
    def showFirstUnique(self) -> int: #O(1)
        if len(self.unique)==0: return -1
        return next(iter(self.unique))

    def add(self, value: int) -> None: #~O(1)
        if value not in self.visited:
            self.unique[value]=True
        elif value in self.unique:
            del self.unique[value]
        self.visited[value] = True
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

"""
def showFirstUnique(self) -> int:
a=iter(self.unique)
try:
    b=next(a)
    while self.unique[b]!=1:
        b=next(a)
    return b
except StopIteration:
    return -1
"""