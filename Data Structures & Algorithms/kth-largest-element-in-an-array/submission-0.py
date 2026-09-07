class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            if len(minHeap) < k or minHeap[0] < num:
                heapq.heappush(minHeap, num)
                if len(minHeap) > k:
                    heapq.heappop(minHeap)

        return minHeap[0]