class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        minHeap = []

        for num in count:
            if len(minHeap) < k or count[num] > minHeap[0][0]:
                heapq.heappush(minHeap,(count[num], num))
                if len(minHeap) > k:
                    heapq.heappop(minHeap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res