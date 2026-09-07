class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num: int) -> int:
    
        if len(self.minHeap) < self.k or num > self.minHeap[0] :
            heapq.heappush(self.minHeap, num)
            if len(self.minHeap) > self.k:
                heapq.heappop(self.minHeap)

        return self.minHeap[0]