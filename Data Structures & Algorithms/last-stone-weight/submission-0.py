class Solution:
    def lastStoneWeight(self, arr: List[int]) -> int:
        
        arr = [i*-1 for i in arr]
        heapq.heapify(arr)

        while len(arr) > 1:
            y = -heapq.heappop(arr)
            x = -heapq.heappop(arr)

            new_weight = y - x
            if new_weight != 0:
                heapq.heappush(arr, -new_weight)
                    
        if arr:
            return -arr[0]
        else:
            return 0