class Solution:
    def getDistance(self, point):
        x,y = point
        return ((x ** 2) + (y ** 2)) ** 0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for point in points:
            dist = self.getDistance(point)
            
            if len(maxHeap) < k or -dist > maxHeap[0][0]:
                heapq.heappush(maxHeap, [-dist, point])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        
        res = []
        while maxHeap:
            dist, point = heapq.heappop(maxHeap)
            res.append(point)
        
        return res
