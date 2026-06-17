class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
 
       
        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            heavy = heapq.heappop(stones)
            if heaviest == heavy:
                continue
            if heavy > heaviest:
                heapq.heappush(stones, heaviest - heavy )
        
        if len(stones) == 0:
            return 0
        
        return -1 * stones[0]

            