class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            print(stones)
            stones.sort(reverse=True)
            i=0
            print(stones)
            while i < len(stones)-1:
                stones[i] = stones[i]-stones[i+1]
                stones.pop(i+1)
                i+=1
        if stones:
            return stones[0]
        return 0
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            diff = stones[0]-stones[1]
            if diff:
                stones.append(diff)
            stones.pop(0)
            stones.pop(0)
        return 0 if stones==[] else stones[0]
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            diff = stones[0]-stones[1]
            if diff: stones.append(diff)
            stones = stones[2:]
        if stones: return stones[0]
        return 0